import os
import pickle
import math
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from allocation.models import Allocate_Mentor

MODEL_PATH = os.path.join("allocation", "prediction", "allocation_model.pkl")


# -------------------------
# Train ML model
# -------------------------
def train_allocation_model():
    """Train mentor regression model with main and alt domains"""
    records = Allocate_Mentor.objects.all().values()
    if not records:
        print("❌ No data available to train")
        return None

    df = pd.DataFrame(records)
    df["mentor_alt_domains"] = df["mentor_alt_domains"].fillna("").apply(lambda x: x.split(",") if x else [])

    # Encode main domains
    team_encoder = LabelEncoder()
    mentor_encoder = LabelEncoder()
    df["team_domain_enc"] = team_encoder.fit_transform(df["team_domain"])
    df["mentor_domain_enc"] = mentor_encoder.fit_transform(df["mentor_domain"])

    # One-hot encode alt domains
    mlb = MultiLabelBinarizer()
    alt_encoded = mlb.fit_transform(df["mentor_alt_domains"])
    alt_df = pd.DataFrame(alt_encoded, columns=mlb.classes_)
    df = pd.concat([df, alt_df], axis=1)

    # Encode experience
    exp_map = {"Beginner": 1, "Expert": 2}
    df["mentor_experience_enc"] = df["mentor_experience"].map(exp_map).fillna(0)

    # Features and target
    X = df[["team_domain_enc", "mentor_domain_enc", "mentor_experience_enc"] + list(mlb.classes_)]
    y = df["similarity_score"].values

    mentor_model = RandomForestRegressor(n_estimators=100, random_state=42)
    mentor_model.fit(X, y)

    # Save model + encoders + dataset + alt ML encoder
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((mentor_model, team_encoder, mentor_encoder, mlb, df), f)

    print("✅ Model trained and saved at:", MODEL_PATH)
    return mentor_model, team_encoder, mentor_encoder, mlb, df


# -------------------------
# Helper: Predict similarity
# -------------------------
def get_similarity_score(mentor_model, team, mentor, encoders, df_similarity):
    team_encoder, mentor_encoder, mlb = encoders
    team_domain = team["domain"]
    mentor_domain = mentor["domain"]
    mentor_experience = mentor.get("experience")

    # Check dataset first
    match = df_similarity[
        (df_similarity['team_domain'] == team_domain) &
        (df_similarity['mentor_domain'] == mentor_domain) &
        (df_similarity['mentor_experience'] == mentor_experience)
    ]
    if not match.empty:
        record = match.iloc[0]
        return record['similarity_score'], record.get('reason', "Exact match")

    # Encode features for prediction
    try:
        team_enc = team_encoder.transform([team_domain])[0]
        mentor_enc = mentor_encoder.transform([mentor_domain])[0]
    except ValueError:
        # unseen domain(s) — return a low fallback score
        return 0.1, "Predicted match (unseen domain)"

    exp_enc = 2 if mentor_experience == "Expert" else 1

    # One-hot encode mentor alt domains (safe transform)
    alt_list = mentor.get("alt_domains", [])
    try:
        alt_vector = mlb.transform([alt_list])[0]
    except Exception:
        # if transform fails for any reason (unknown classes), fall back to zeros
        alt_vector = np.zeros(len(mlb.classes_), dtype=int)

    # Combine features
    X_pred = np.array([team_enc, mentor_enc, exp_enc] + alt_vector.tolist()).reshape(1, -1)
    sim_score = float(mentor_model.predict(X_pred)[0])
    return sim_score, "Predicted match"


# -------------------------
# Fully ML-driven Allocation (two-round)
# -------------------------
def allocate_mentors_ml(teams, mentors, max_teams_per_mentor=None):
    """
    Two-round ML allocation:
      - Round 1: strict one-to-one (each mentor at most 1 team) using ML-scores (greedy global).
      - Round 2: fill remaining teams allowing mentors to take more up to capacity.
    If max_teams_per_mentor is None, capacity = ceil(#teams / #mentors).
    """
    if not os.path.exists(MODEL_PATH):
        train_allocation_model()

    with open(MODEL_PATH, "rb") as f:
        mentor_model, team_encoder, mentor_encoder, mlb, df_similarity = pickle.load(f)

    encoders = (team_encoder, mentor_encoder, mlb)

    # 1) build all pairs with ML-predicted similarity
    all_pairs = []
    for t_idx, team in enumerate(teams):
        for m_idx, mentor in enumerate(mentors):
            sim_score, reason = get_similarity_score(mentor_model, team, mentor, encoders, df_similarity)
            all_pairs.append({
                "team_idx": t_idx,
                "mentor_idx": m_idx,
                "mentor_id": mentor["id"],
                "sim_score": sim_score,
                "team": team,
                "mentor": mentor,
                "reason": reason
            })

    # sort globally by sim_score (desc)
    all_pairs.sort(key=lambda x: x["sim_score"], reverse=True)

    # prepare bookkeeping
    mentor_load = {mentor["id"]: 0 for mentor in mentors}
    assigned_teams = set()
    assigned_mentors = set()
    allocations = []

    # ---------- Round 1: strict one-to-one ----------
    for pair in all_pairs:
        t_idx = pair["team_idx"]
        m_id = pair["mentor_id"]

        if t_idx not in assigned_teams and m_id not in assigned_mentors:
            # assign team -> mentor (one-to-one)
            assigned_teams.add(t_idx)
            assigned_mentors.add(m_id)
            mentor_load[m_id] += 1
            allocations.append({
                "Team": pair["team"].get("name", pair["team"].get("id")),
                "Team Domain": pair["team"]["domain"],
                "Mentor": pair["mentor"].get("name", pair["mentor"].get("id")),
                "Mentor Domain": pair["mentor"]["domain"],
                "Mentor Alt Domains": ", ".join(pair["mentor"].get("alt_domains", [])),
                "Experience": pair["mentor"].get("experience", "-"),
                "Similarity Score": round(pair["sim_score"], 3),
                "Reason": pair["reason"]
            })

    # If everything assigned in round 1, done
    if len(assigned_teams) == len(teams):
        return pd.DataFrame(allocations)

    # ---------- Round 2: fill remaining teams up to capacity ----------
    if max_teams_per_mentor is None:
        max_capacity = max(1, math.ceil(len(teams) / len(mentors)))
    else:
        max_capacity = max(1, int(max_teams_per_mentor))

    # Greedy second pass: allow mentors to take additional teams up to max_capacity
    for pair in all_pairs:
        t_idx = pair["team_idx"]
        m_id = pair["mentor_id"]

        if t_idx in assigned_teams:
            continue

        if mentor_load[m_id] < max_capacity:
            # assign this remaining team to this mentor
            assigned_teams.add(t_idx)
            mentor_load[m_id] += 1
            allocations.append({
                "Team": pair["team"].get("name", pair["team"].get("id")),
                "Team Domain": pair["team"]["domain"],
                "Mentor": pair["mentor"].get("name", pair["mentor"].get("id")),
                "Mentor Domain": pair["mentor"]["domain"],
                "Mentor Alt Domains": ", ".join(pair["mentor"].get("alt_domains", [])),
                "Experience": pair["mentor"].get("experience", "-"),
                "Similarity Score": round(pair["sim_score"], 3),
                "Reason": pair["reason"]
            })

        # stop early if all teams done
        if len(assigned_teams) == len(teams):
            break

    # Any remaining unassigned teams (should be rare if capacity computed sensibly)
    for t_idx, team in enumerate(teams):
        if t_idx not in assigned_teams:
            allocations.append({
                "Team": team.get("name", team.get("id")),
                "Team Domain": team.get("domain", "-"),
                "Mentor": "-",
                "Mentor Domain": "-",
                "Mentor Alt Domains": "",
                "Experience": "-",
                "Similarity Score": 0,
                "Reason": "No mentor left"
            })

    # Optionally: you can return mentor_load for diagnostics too. For now return allocations DF.
    df_alloc = pd.DataFrame(allocations)

    # Sort results in a readable order (optional) - e.g., by Team
    try:
        df_alloc = df_alloc.sort_values(by="Team").reset_index(drop=True)
    except Exception:
        pass

    return df_alloc


# -------------------------
# Example Test Run (use your data)
# -------------------------
if __name__ == "__main__":
    teams = [
        {"id": 10, "domain": "AIDS"},
        {"id": 11, "domain": "CYS"},
        {"id": 12, "domain": "CD"},
        {"id": 13, "domain": "BW"}
    ]

    mentors = [
        {"id": 1, "domain": "AIML", "experience": "Beginner", "alt_domains": ["AIML,AI,FS"]},
        {"id": 2, "domain": "FS", "experience": "Beginner", "alt_domains": ["CD,AI,FS"]},
        {"id": 3, "domain": "BW", "experience": "Beginner", "alt_domains": ["CYS,BW,FS"]}
    ]

    # Train and allocate (will use your DB-backed Allocate_Mentor data)
    train_allocation_model()
    df_alloc = allocate_mentors_ml(teams, mentors)
    print(df_alloc)
