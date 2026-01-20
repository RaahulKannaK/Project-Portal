
import json,os,time,re
from django.shortcuts import render,get_object_or_404, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import logout # type: ignore
from django.http import JsonResponse # type: ignore
from .models import Student, Mentor_Login, Stu_Login,Team,Mentor,AllocationResult,Coordinator_Login
from django.conf import settings # type: ignore
from .train import allocate_mentors_ml
from django.http import JsonResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from docx import Document # type: ignore
from django.http import FileResponse, Http404

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Team, ApprovedTeam, ModifyRequest



# ---------------------
# Domain Normalization
# ---------------------
DOMAIN_MAP = {
    "AI": "Artificial Intelligence",
    "ARTIFICIAL INTELLIGENCE": "Artificial Intelligence",

    "ML": "Machine Learning",
    "MACHINE LEARNING": "Machine Learning",

    "BW": "Blockchain",
    "BLOCKCHAIN": "Blockchain",

    "CYS": "Cybersecurity",
    "CYBERSECURITY": "Cybersecurity",

    "CD": "Cloud DevOps",
    "CLOUD DEVOPS": "Cloud DevOps",

    "DS": "Data Science",
    "DATA SCIENCE": "Data Science",

    "FS": "Full Stack",
    "FULL STACK": "Full Stack",
}


def get_class_from_roll(roll):
    if roll.startswith("24UCS1"): return "CSE-A"
    elif roll.startswith("24UCS2"): return "CSE-B"
    elif roll.startswith("24UIT"): return "IT"
    elif roll.startswith("24UECE"): return "ECE"
    return "Unknown"


def normalize_domain(text: str):
    if not text:
        return ""
    cleaned = text.strip().upper()
    return DOMAIN_MAP.get(cleaned, cleaned.title())


def normalize_experience(exp: str):
    if not exp:
        return "Beginner"
    exp = exp.strip().lower()
    return "Expert" if "expert" in exp else "Beginner"


# ---------------------
# Login & Dashboards
# ---------------------
def login_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if role == "student":
            try:
                login_data = Stu_Login.objects.get(username=username, password=password)
                student = Student.objects.get(student_id=username)
                request.session.update({
                    "student_id": student.student_id,
                    "student_name": student.name,
                    "student_cgpa": str(student.cgpa),
                    "student_class": get_class_from_roll(username)
                })
                return redirect("student_dashboard")
            except (Stu_Login.DoesNotExist, Student.DoesNotExist):
                messages.error(request, "Invalid student credentials or profile not found")

        elif role == "mentor":
            try:
                mentor = Mentor_Login.objects.get(username=username, password=password)
                request.session.update({
                    "mentor_id": mentor.id,
                    "username": mentor.username,
                    "mentor_name": mentor.name
                })
                return redirect("mentor_dashboard")
            except Mentor_Login.DoesNotExist:
                messages.error(request, "Invalid mentor credentials")

        elif role == "hod":
            try:
                mentor = Mentor_Login.objects.get(username=username, password=password)
                request.session.update({
                    "mentor_id": mentor.id,
                    "username": mentor.username,
                    "mentor_name": mentor.name
                })
                return redirect("hod_dashboard")
            except Mentor_Login.DoesNotExist:
                messages.error(request, "Invalid mentor credentials")
        elif role == "coordinator":
            try:
                coordinator = Coordinator_Login.objects.get(username=username, password=password)
                request.session.update({
                    "coordinator_id": coordinator.id,
                    "username": coordinator.username,
                    "mentor_name": coordinator.name
                })
                return redirect("coordinator_dashboard")
            except Coordinator_Login.DoesNotExist:
                messages.error(request, "Invalid mentor credentials")


        else:
            messages.error(request, "Invalid role selected")

    return render(request, "accounts/login.html")


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import AnnouncementStatus

from django.db.models import Prefetch

def student_dashboard(request):
    # =====================================================
    # 🔐 SESSION CHECK (ORIGINAL - UNCHANGED)
    # =====================================================
    student_id = request.session.get("student_id")
    username = request.session.get("username")
    student_name = request.session.get("student_name")

    if not student_id:
        return redirect("login")

    print(f"[DEBUG] Student: {student_name}, Username: {username}")

    # =====================================================
    # 🔹 FETCH ANNOUNCEMENTS FOR STUDENT
    # =====================================================
    announcement_qs = AnnouncementStatus.objects.filter(
        receiver_role="student",
        receiver_id=student_id
    ).select_related("announcement").order_by(
        "-announcement__created_at"
    )

    # =====================================================
    # 🆕 LATEST ANNOUNCEMENT (OLD LOGIC - PRESERVED)
    # =====================================================
    latest_announcement = announcement_qs.first()

    # =====================================================
    # 🆕 ALL ANNOUNCEMENTS (UPGRADE – NEW FEATURE)
    # =====================================================
    all_announcements = announcement_qs

    print(
        f"[DEBUG] Latest announcement:",
        latest_announcement.announcement.title if latest_announcement else "None"
    )
    print(f"[DEBUG] Total announcements:", all_announcements.count())

    # =====================================================
    # 🔁 OTHER EXISTING DASHBOARD LOGIC
    # (KEEP EVERYTHING YOU ALREADY HAVE BELOW)
    # =====================================================
    # example placeholders – DO NOT REMOVE YOUR OWN CODE
    notifications = []
    profile_data = {}

    # =====================================================
    # 🎯 FINAL CONTEXT
    # =====================================================
    context = {
        "student_name": student_name,
        "username": username,

        # 🔔 ANNOUNCEMENTS
        "latest_announcement": latest_announcement,   # OUTSIDE BOX
        "all_announcements": all_announcements,       # BUTTON VIEW

        # 🔁 KEEP OLD DATA
        "notifications": notifications,
        "profile_data": profile_data,
    }

    return render(request, "student/stu_dash.html", context)

from django.views.decorators.http import require_POST

@require_POST
def acknowledge_announcement(request, status_id):
    status = get_object_or_404(
        AnnouncementStatus,
        id=status_id,
        receiver_role="student"
    )

    if status.acknowledged_at is None:
        status.acknowledged_at = timezone.now()
        status.save()

    return redirect("student_dashboard")

def mentor_dashboard(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    return render(request, "mentor/men_dash.html", {
        "mentor_name": mentor_name,
        "username": username,
    })

def hod_dashboard(request):
    return render(request, "accounts/hod_dash.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Announcement,AnnouncementStatus
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone


def coordinator_dashboard(request):

    # 🔐 SESSION CHECK (VERY IMPORTANT)
    coordinator_id = request.session.get("coordinator_id")
    if not coordinator_id:
        return redirect("login")

    coordinator = get_object_or_404(Coordinator_Login, id=coordinator_id)

    # =========================================================
    # 📢 CREATE ANNOUNCEMENT
    # =========================================================
    if request.method == "POST":

        print("POST DATA:", request.POST)

        title = request.POST.get("title")
        ann_type = request.POST.get("ann_type")        # deadline / schedule / instruction
        target = request.POST.get("target")            # student / mentor / both

        deadline_date = request.POST.get("deadline_date")
        deadline_time = request.POST.get("deadline_time")

        schedule_date = request.POST.get("schedule_date")
        schedule_time = request.POST.get("schedule_time")
        venue = request.POST.get("venue")

        message = request.POST.get("message")

        # -----------------------------------------------------
        # COMMON VALIDATION
        # -----------------------------------------------------
        if not title or not ann_type or not target:
            messages.error(request, "Please fill all required fields")
            return redirect("coordinator_dashboard")

        # -----------------------------------------------------
        # ANNOUNCEMENT CREATION (BASED ON TYPE)
        # -----------------------------------------------------
        announcement = None

        # 🔔 DEADLINE
        if ann_type == "deadline":
            if not deadline_date or not deadline_time:
                messages.error(request, "Deadline date and time required")
                return redirect("coordinator_dashboard")

            announcement = Announcement.objects.create(
                title=title,
                ann_type=ann_type,
                target_role=target,
                deadline_date=deadline_date,
                deadline_time=deadline_time,
                created_by_username=coordinator.username,
                created_by_name=coordinator.name
            )

        # 🗓️ SCHEDULE
        elif ann_type == "schedule":
            if not schedule_date or not schedule_time or not venue:
                messages.error(request, "Schedule date, time and venue required")
                return redirect("coordinator_dashboard")

            announcement = Announcement.objects.create(
                title=title,
                ann_type=ann_type,
                target_role=target,
                schedule_date=schedule_date,
                schedule_time=schedule_time,
                venue=venue,
                created_by_username=coordinator.username,
                created_by_name=coordinator.name
            )

        # 📝 INSTRUCTION
        elif ann_type == "instruction":
            if not message:
                messages.error(request, "Instruction message required")
                return redirect("coordinator_dashboard")

            announcement = Announcement.objects.create(
                title=title,
                ann_type=ann_type,
                target_role=target,
                message=message,
                created_by_username=coordinator.username,
                created_by_name=coordinator.name
            )

        else:
            messages.error(request, "Invalid announcement type")
            return redirect("coordinator_dashboard")

        # -----------------------------------------------------
        # 🎯 ASSIGN ANNOUNCEMENT TO USERS
        # -----------------------------------------------------
        status_objects = []

        if target == "student":
            students = Student.objects.all()
            for s in students:
                status_objects.append(
                    AnnouncementStatus(
                        announcement=announcement,
                        receiver_role="student",
                        receiver_id=s.student_id,
                        receiver_name=s.name
                    )
                )

        elif target == "mentor":
            mentors = Mentor_Login.objects.all()
            for m in mentors:
                status_objects.append(
                    AnnouncementStatus(
                        announcement=announcement,
                        receiver_role="mentor",
                        receiver_id=m.username,
                        receiver_name=m.name
                    )
                )

        else:  # BOTH
            students = Student.objects.all()
            mentors = Mentor_Login.objects.all()

            for s in students:
                status_objects.append(
                    AnnouncementStatus(
                        announcement=announcement,
                        receiver_role="student",
                        receiver_id=s.student_id,
                        receiver_name=s.name
                    )
                )

            for m in mentors:
                status_objects.append(
                    AnnouncementStatus(
                        announcement=announcement,
                        receiver_role="mentor",
                        receiver_id=m.username,
                        receiver_name=m.name
                    )
                )

        AnnouncementStatus.objects.bulk_create(status_objects)

        messages.success(request, "Announcement circulated successfully!")
        return redirect("coordinator_dashboard")

    # =========================================================
    # 📊 LOAD DASHBOARD DATA
    # =========================================================
    announcements = Announcement.objects.filter(
        created_by_username=coordinator.username
    ).order_by("-created_at")

    return render(request, "coordinator/coord_dash.html", {
        "coordinator": coordinator,
        "announcements": announcements
    })

def logout_view(request):
    logout(request)
    return redirect("login")


@csrf_exempt
def create_team(request):
    student_class = request.session.get("student_class")
    student_id = request.session.get("student_id")

    # collect all members already used in any team
    used_rolls = []
    for t in Team.objects.all():
        if t.members:
            used_rolls.extend(t.members.split(","))

    # classmates list (only free students)
    classmates = Student.objects.filter(clas=student_class).exclude(student_id__in=used_rolls)

    # check if this student already has a team
    existing_team = None
    for t in Team.objects.filter(student_class=student_class):
        if t.members and student_id in t.members.split(","):
            existing_team = t
            break
    already_created = existing_team is not None

    # -----------------------------
    # Handle form submission (POST)
    # -----------------------------
    if request.method == "POST":
        try:
            # ✅ Read JSON safely regardless of content type
            body = request.body.decode("utf-8")
            data = json.loads(body) if body else {}

            print("📦 Received data:", data)

            project_title = str(data.get("project_title", "")).strip()
            domain_raw = data.get("domain", "")
            print(domain_raw)
            domain = domain_raw.upper() if domain_raw else ""
            members = data.get("members", [])

            # 🧩 Validation checks
            if not project_title:
                return JsonResponse({"status": "error", "message": "⚠ Project title is required."})

            if not domain:
                return JsonResponse({"status": "error", "message": "⚠ Domain is required."})

            if not members:
                return JsonResponse({"status": "error", "message": "⚠ No members selected."})

            # include leader (logged-in student)
            all_members = set(members)
            all_members.add(student_id)

            # check if logged-in student is part of the submitted members
            if student_id not in all_members:
                return JsonResponse({
                    "status": "error",
                    "message": "⚠ The user didn't involve in the team!"
                })

            # check if any members are already used
            already_used = [m for m in all_members if m in used_rolls]
            if already_used:
                return JsonResponse({
                    "status": "error",
                    "message": f"⚠ Student(s) {', '.join(already_used)} already in a team."
                })

            # check if this student already created a team
            if already_created:
                return JsonResponse({
                    "status": "error",
                    "message": "⚠ You have already created a team."
                })

            # check for duplicate project titles
            if Team.objects.filter(project_title__iexact=project_title).exists():
                return JsonResponse({
                    "status": "error",
                    "message": "⚠ Project title already exists. Please choose another."
                })

            # ✅ Get names of selected members
            member_objs = Student.objects.filter(student_id__in=all_members)
            member_names = [s.name for s in member_objs]

            # ✅ Create team with project title
            Team.objects.create(
                project_title=project_title,
                student_class=student_class,
                domain=domain,
                members=",".join(all_members),
                member_names=",".join(member_names)
            )

            return JsonResponse({"status": "success", "project_title": project_title})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data received."})
        except Exception as e:
            print("❌ Exception in create_team:", e)
            return JsonResponse({"status": "error", "message": str(e)})

    # -----------------------------
    # Prepare page data for render
    # -----------------------------
    members_list = []
    if existing_team and existing_team.members:
        ids = existing_team.members.split(",")
        members_list = list(
            Student.objects.filter(student_id__in=ids).values_list("student_id", "name")
        )

    return render(request, "student/create_team.html", {
        "classmates": classmates,
        "student_class": student_class,
        "already_created": already_created,
        "existing_team": existing_team,
        "members_list": members_list,
    })


def view_mentor(request):
    return render(request, "accounts/view_mentor.html")

def add_men(request):
    if "mentor_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not logged in"}, status=401)

    mentor_created = False
    primary_domain = experience = alternative_domains_list = ""
    username = mentor_name = None

    username = request.session.get("username")
    mentor_name = request.session.get("mentor_name")

    try:
        mentor = Mentor.objects.get(username=username)
        mentor_created = True
        primary_domain = mentor.primary_domain
        experience = mentor.experience
        # Split alternative domains into list for template
        alternative_domains_list = mentor.alternative_domains.split(",") if mentor.alternative_domains else []
    except Mentor.DoesNotExist:
        pass

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            primary_domain = data.get("primary_domain")
            experience = data.get("experience")
            alt_domains = data.get("alt_domains", [])
            alternative_domains = ",".join(alt_domains)

            Mentor.objects.update_or_create(
                username=username,
                defaults={
                    "name": mentor_name,
                    "primary_domain": primary_domain,
                    "experience": experience,
                    "alternative_domains": alternative_domains
                }
            )

            return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    context = {
        "mentor_created": mentor_created,
        "primary_domain": primary_domain,
        "experience": experience,
        "alternative_domains": alternative_domains_list,
        "username": username,
        "mentor_name": mentor_name
    }
    return render(request, "mentor/add_men.html", context)

def allocate_view(request):
    # ---------------------
    # Fetch teams from DB
    # ---------------------
    teams_qs = Team.objects.all()
    teams = [{"id": t.id, "name": t.project_title, "domain": t.domain} for t in teams_qs]
    print("✅ Teams fetched from DB:", teams)

    if not teams:
        return render(request, "accounts/allocation_result.html", {
            "allocations": [],
            "error": "No teams available."
        })

    # ---------------------
    # Fetch mentors from DB
    # ---------------------
    mentors_qs = Mentor.objects.all()
    mentors = []
    for m in mentors_qs:
        mentors.append({
            "id": m.id,
            "domain": m.primary_domain,
            "name": m.name,
            "experience": "Expert" if m.experience >= 4 else "Beginner",
            "alt_domains": m.alternative_domains.split(",") if m.alternative_domains else []
        })
    print("✅ Mentors fetched from DB:", mentors)

    if not mentors:
        return render(request, "accounts/allocation_result.html", {
            "allocations": [],
            "error": "No mentors available."
        })

    # ---------------------
    # ML Allocation
    # ---------------------
    allocations_df = allocate_mentors_ml(teams, mentors)
    print("✅ Allocations DataFrame:\n", allocations_df)

    # ---------------------
    # Rename columns for template & DB
    # ---------------------
    allocations_df.rename(columns={
        "Team": "team_name",
        "Team Domain": "team_domain",
        "Mentor": "mentor_name",
        "Mentor Domain": "mentor_domain",
        "Mentor Alt Domains": "alt_domains",
        "Experience": "experience",
        "Similarity Score": "similarity_score",
        "Reason": "reason"
    }, inplace=True)

    # Convert alt_domains to comma-separated strings
    allocations_df["alt_domains"] = allocations_df["alt_domains"].fillna("").apply(
        lambda x: x if isinstance(x, str) else ", ".join(x)
    )

    # ---------------------
    # Save allocations to DB
    # ---------------------
    for _, row in allocations_df.iterrows():
        AllocationResult.objects.update_or_create(
            team_name=row["team_name"],
            defaults={
                "team_domain": row["team_domain"],
                "mentor_name": row["mentor_name"],
                "mentor_domain": row["mentor_domain"],
                "alt_domains": row["alt_domains"],
                "experience": row["experience"],
                "similarity_score": row["similarity_score"],
                "reason": row["reason"]
            }
        )

    # ---------------------
    # Prepare template data
    # ---------------------
    allocations = allocations_df.to_dict(orient="records")
    print("✅ Allocations list for template:", allocations)

    return render(request, "accounts/allocation_result.html", {"allocations": allocations})

def zero_men(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    team_members = []
    team_name = None

    # Get the latest allocation for this mentor
    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).order_by('-allocated_at').first()
    if allocation:
        team_name = allocation.team_name
        # Fetch the team object using project_title instead of team_name
        team = Team.objects.filter(project_title=team_name).first()
        if team and team.member_names:
            team_members = team.member_names.split(",")

    return render(request, "mentor/review_men/zero_men.html", {
        "mentor_name": mentor_name,
        "username": username,
        "team_name": team_name,
        "team_members": team_members,
    })

def one_men(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    team_members = []
    team_name = None

    # Get the latest allocation for this mentor
    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).order_by('-allocated_at').first()
    if allocation:
        team_name = allocation.team_name
        # Fetch the team object using project_title instead of team_name
        team = Team.objects.filter(project_title=team_name).first()
        if team and team.member_names:
            team_members = team.member_names.split(",")

    return render(request, "mentor/review_men/1_men.html", {
        "mentor_name": mentor_name,
        "username": username,
        "team_name": team_name,
        "team_members": team_members,
    })

def two_men(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    return render(request,  "mentor/review_men/2_men.html", {
        "mentor_name": mentor_name,
        "username": username,
    })

def three_men(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    return render(request,  "mentor/review_men/3_men.html", {
        "mentor_name": mentor_name,
        "username": username,
    })

def zero_doc(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    return render(request,  "mentor/review_men/men_doc/zero_paper/zero_doc.html", {
        "mentor_name": mentor_name,
        "username": username,
    })

def serve_pdf(request, team_name, pdf_type):
    """
    Serve the requested PDF in iframe.
    pdf_type: 'Abstract', 'FullPaper', 'Review', etc.
    """
    team_folder = team_name.replace(" ", "_")
    pdf_file = f"{team_folder}_{pdf_type}.pdf"
    pdf_full_path = os.path.join(settings.MEDIA_ROOT, team_folder, pdf_file)

    if not os.path.exists(pdf_full_path):
        raise Http404("PDF not found")

    response = FileResponse(open(pdf_full_path, 'rb'), content_type='application/pdf')
    response['X-Frame-Options'] = 'ALLOWALL'  # allow iframe embedding
    return response

import os
import re
import subprocess
import pdfplumber

from django.conf import settings
from django.shortcuts import render
from .models import AllocationResult


# --------------------------------------------------
# 🔍 HEADING VALIDATION (STRICT)
# --------------------------------------------------
def is_valid_heading(text):
    text = text.strip()

    # Reject bullets
    if text.startswith(("-", "•")):
        return False

    # Reject numbered lists
    if re.match(r"^\d+[\.\)]", text):
        return False

    # Reject long sentences
    if len(text) > 70:
        return False

    # ❌ Reject sentence-like endings
    if text.endswith("."):
        return False

    # ❌ Reject colon-ended sub-points
    if text.endswith(":"):
        return False

    # ❌ Reject mid-sentence lowercase patterns
    if any(word.islower() for word in text.split()[1:]):
        return False

    # Must contain at least ONE capitalized word
    return any(word[0].isupper() for word in text.split() if word)


# --------------------------------------------------
# 🧠 EARLY PAGE HEADING DETECTOR
# (Abstract / Introduction / Problem Statement)
# --------------------------------------------------
def looks_like_early_heading(text, top, page_no):
    text = text.strip()

    early_keywords = {
        "abstract",
        "introduction",
        "problem statement",
        "background",
        "motivation"
    }

    if text.lower() in early_keywords:
        return True

    # Reject colon endings here too
    if text.endswith(":"):
        return False

    if (
        page_no <= 2
        and len(text.split()) <= 4
        and text[0].isupper()
        and not text.endswith(".")
    ):
        return True

    return False

# --------------------------------------------------
# 🎯 MAIN VIEW
# --------------------------------------------------
import os
import subprocess
import json
import pdfplumber

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction
from allocation.models import AllocationResult
from allocation.models import ZerothReviewRemark


import json
from django.http import JsonResponse

def zero_review(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")

    # =====================================================
    # POST → SAVE ZEROTH REVIEW (NO DUPLICATES - FINAL FIX)
    # =====================================================
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            remarks = data.get("remarks", [])

            allocation = AllocationResult.objects.filter(
                mentor_name=mentor_name
            ).first()

            if not allocation:
                return JsonResponse(
                    {"status": "fail", "message": "Team not found"},
                    status=404
                )

            team_name = allocation.team_name
            inserted = 0
            skipped = 0

            for r in remarks:
                heading = r.get("heading", "").strip()
                remark = r.get("remark", "").strip()
                color = r.get("color", "").strip()

                try:
                    with transaction.atomic():
                        _, created = ZerothReviewRemark.objects.get_or_create(
                            team_name=team_name,
                            mentor_name=mentor_name,
                            heading=heading,
                            remark=remark,
                            color=color
                        )

                        if created:
                            inserted += 1
                        else:
                            skipped += 1

                except IntegrityError:
                    # DB-level duplicate protection
                    skipped += 1

            return JsonResponse({
                "status": "success",
                "inserted": inserted,
                "skipped": skipped
            })

        except Exception as e:
            print("❌ Zeroth review save error:", e)
            return JsonResponse(
                {"status": "fail", "message": str(e)},
                status=500
            )

    # =====================================================
    # ---------------- EXISTING GET LOGIC -----------------
    # (UNCHANGED — DO NOT TOUCH)
    # =====================================================
    html_path = None
    allocation = AllocationResult.objects.filter(
        mentor_name=mentor_name
    ).first()

    if not allocation:
        return render(
            request,
            "mentor/review_men/men_doc/zero_paper/zero_review.html"
        )

    team_name = allocation.team_name
    folder_name = team_name.replace(" ", "_")

    pdf_file = f"{folder_name}_Abstract.pdf"
    pdf_dir = os.path.join(settings.BASE_DIR, "project_docs", folder_name)
    html_dir = os.path.join(pdf_dir, "html")
    pdf_fs_path = os.path.join(pdf_dir, pdf_file)

    os.makedirs(html_dir, exist_ok=True)

    html_files = (
        [f for f in os.listdir(html_dir) if f.lower().endswith(".html")]
        if os.path.exists(html_dir) else []
    )

    if os.path.exists(pdf_fs_path) and not html_files:
        try:
            subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-v", f"{pdf_dir}:/pdf",
                    "pdf2html_local",
                    pdf_file,
                    "--dest-dir", "html"
                ],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print("[ERROR] PDF → HTML failed:", e)

    if os.path.exists(html_dir):
        for f in os.listdir(html_dir):
            if f.lower().endswith(".html"):
                html_path = f"/project_docs/{folder_name}/html/{f}"
                break

    main_heading_lines = []
    sub_headings = []

    try:
        with pdfplumber.open(pdf_fs_path) as pdf:
            for page_no, page in enumerate(pdf.pages, start=1):
                chars = page.chars
                if not chars:
                    continue

                lines = {}
                for ch in chars:
                    top = round(ch["top"], 1)
                    lines.setdefault(top, []).append(ch)

                merged_lines = []
                for top, chs in lines.items():
                    text = "".join(
                        c["text"] for c in sorted(chs, key=lambda x: x["x0"])
                    ).strip()
                    size = round(
                        sum(c["size"] for c in chs) / len(chs),
                        1
                    )
                    merged_lines.append((top, size, text))

                sizes = [s for _, s, t in merged_lines if t]
                if not sizes:
                    continue

                max_size = max(sizes)

                for top, size, text in merged_lines:
                    if not text:
                        continue

                    if page_no == 1 and abs(size - max_size) < 0.5:
                        main_heading_lines.append(text)

                    elif (
                        size >= max_size * 0.8 and is_valid_heading(text)
                    ) or looks_like_early_heading(text, top, page_no):
                        if text not in sub_headings:
                            sub_headings.append(text)

    except Exception as e:
        print("[ERROR] Heading detection failed:", e)

    main_heading = " ".join(main_heading_lines).strip()

    return render(
        request,
        "mentor/review_men/men_doc/zero_paper/zero_review.html",
        {
            "mentor_name": mentor_name,
            "username": username,
            "html_path": html_path,
            "team_name": team_name,
            "main_heading": main_heading,
            "sub_headings": sub_headings,
        }
    )

def zero_base(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    return render(request,  "mentor/review_men/men_doc/zero_paper/zero_base.html", {
        "mentor_name": mentor_name,
        "username": username,
    })
def zero_form(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    pdf_path = None

    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).first()

    if allocation:
        team_name = allocation.team_name
        print(f"[DEBUG] Allocated team found for mentor '{mentor_name}': {team_name}")
        
        # Explicitly pass pdf_type = 'Abstract'
        pdf_path = f"/mentor/pdf/{team_name}/Report/"
    else:
        print(f"[DEBUG] No allocated team found for mentor '{mentor_name}'")

    return render(request, "mentor/review_men/men_doc/zero_paper/zero_form.html", {
        "mentor_name": mentor_name,
        "username": username,
        "pdf_path": pdf_path,
        "team_name": allocation.team_name if allocation else None
    })

def zero_ppt(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    ppt_path = None

    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).first()

    if allocation:
        team_name = allocation.team_name
        team_folder = team_name.replace(" ", "_")
        ppt_file = f"{team_folder}_PPT.pptx"  # <- corrected file name
        ppt_full_path = os.path.join(settings.MEDIA_ROOT, team_folder, ppt_file)

        if os.path.exists(ppt_full_path):
            ppt_path = f"{settings.MEDIA_URL}{team_folder}/{ppt_file}"
            print(f"[DEBUG] PPT found at: {ppt_full_path}")
        else:
            print(f"[DEBUG] PPT NOT found at: {ppt_full_path}")
    else:
        print(f"[DEBUG] No allocated team found for mentor '{mentor_name}'")

    return render(request, "mentor/review_men/men_doc/zero_paper/zero_ppt.html", {
        "mentor_name": mentor_name,
        "username": username,
        "ppt_path": ppt_path,
        "team_name": allocation.team_name if allocation else None
    })


def zero_ma(request, team_name):
    team_members = []
    
    # Fetch team object using project_title
    team = Team.objects.filter(project_title=team_name).first()
    if team and team.member_names:
        # Convert comma-separated string to list
        team_members = team.member_names.split(",")

    # Render the zero_ma page for a specific team
    return render(request, 'mentor/review_men/men_ma/zero_ma.html', {
        'team_name': team_name,
        'team_members': team_members
    })

def one_ma(request, team_name):
    team_members = []
    
    # Fetch team object using project_title
    team = Team.objects.filter(project_title=team_name).first()
    if team and team.member_names:
        # Convert comma-separated string to list
        team_members = team.member_names.split(",")

    # Render the Review 1 (mentor assessment) page for a specific team
    return render(request, 'mentor/review_men/men_ma/one_ma.html', {
        'team_name': team_name,
        'team_members': team_members
    })


def men_ppt(request):
    return render(request, "mentor/review_men/men_doc/first_paper/ppt.html")

def zero_stu(request):
    student_name = request.session.get("student_name")
    print(student_name)
    username = request.session.get("username")
    team = Team.objects.filter(member_names__icontains=student_name).first()
    if not team:
        return JsonResponse({"status": "fail", "message": "Team not found for this student"}, status=404)

    project_title = team.project_title.replace(" ", "_")  # sanitize for filename

    return render(request, "student/review/zero_stu.html", {
        "student_name": student_name,
        "username": username,
        "team_name": project_title,
    })
def one_stu(request):
    return render(request, "student/review/1_stu.html")

def two_stu(request):
    return render(request, "student/review/2_stu.html")

def three_stu(request):
    return render(request, "student/review/3_stu.html")


def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, "coordinator/men_list.html", {"mentors": mentors})

def team_list(request):
    # GET request → show page
    if request.method == "GET":
        teams = Team.objects.all()
        approved_teams = ApprovedTeam.objects.all()
        modified_teams = ModifyRequest.objects.all()
        return render(request, "coordinator/team_list.html", {
            "teams": teams,
            "approved_teams": approved_teams,
            "modified_teams": modified_teams
        })

    # POST request → from Confirm button
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            approved = data.get("approved", [])
            modified = data.get("modified", [])

            # ✅ Handle Approved Teams (no duplicates)
            for project_title in approved:
                team = Team.objects.filter(project_title=project_title).first()
                if team and not ApprovedTeam.objects.filter(project_title=project_title).exists():
                    ApprovedTeam.objects.create(
                        project_title=team.project_title,
                        student_class=team.student_class,
                        domain=team.domain,
                        members=team.members,
                        member_names=team.member_names,
                    )

            # ✅ Handle Modified Teams (no duplicates)
            for item in modified:
                project_title = item.get("project")
                change_type = item.get("changeType", "")
                team = Team.objects.filter(project_title=project_title).first()

                # if modification not already requested for this project
                if team and not ModifyRequest.objects.filter(project_title=project_title).exists():
                    ModifyRequest.objects.create(
                        project_title=team.project_title,
                        student_class=team.student_class,
                        domain=team.domain,
                        members=team.members,
                        member_names=team.member_names,
                        change_type=change_type,
                    )

            return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
def approve_team(request, project_title):
    team = get_object_or_404(Team, project_title=project_title)

    # 🧹 Step 1: Remove any pending modify request for same team
    ModifyRequest.objects.filter(project_title=project_title).delete()

    # 🧩 Step 2: Add/update in approved table
    approved, created = ApprovedTeam.objects.update_or_create(
        project_title=team.project_title,
        defaults={
            "student_class": team.student_class,
            "domain": team.domain,
            "members": team.members,
            "member_names": team.member_names,
        }
    )

    if created:
        messages.success(request, f"'{team.project_title}' approved successfully!")
    else:
        messages.info(request, f"'{team.project_title}' was already approved — details updated!")

    return redirect("team_list")

def modify_team(request, project_title):
    if request.method == "POST":
        change_type = request.POST.get("change_type")
        print("Modify triggered:", request.POST)

        team = get_object_or_404(Team, project_title=project_title)

        # 🧹 Step 1: Remove from Approved list if exists
        ApprovedTeam.objects.filter(project_title=project_title).delete()

        # 🧹 Step 2: Remove old modify request (avoid duplicates)
        ModifyRequest.objects.filter(project_title=project_title).delete()

        # 🧩 Step 3: Add new modify request
        ModifyRequest.objects.create(
            project_title=team.project_title,
            student_class=team.student_class,
            domain=team.domain,
            members=team.members,
            member_names=team.member_names,
            change_type=change_type
        )

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"status": "success"})

        messages.success(request, f"Modification request for '{team.project_title}' ({change_type}) added successfully!")
        return redirect("team_list")

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

from allocation.models import ZerothReviewRemark
from allocation.models import Team


@csrf_exempt
def zero_ma1(request):
    # =================================================
    # 👤 Student session details
    # =================================================
    student_name = request.session.get("student_name")
    username = request.session.get("username")

    print(f"[DEBUG] Student: {student_name}, Username: {username}")

    # =================================================
    # 🔍 Find student's team
    # =================================================
    team = Team.objects.filter(
        member_names__icontains=student_name
    ).first()

    if not team:
        print("[DEBUG] Team not found for student")
        return JsonResponse(
            {"status": "fail", "message": "Team not found"},
            status=404
        )

    # -------------------------------------------------
    # DB uses original title (with spaces)
    # File system uses underscore version
    # -------------------------------------------------
    team_title_db = team.project_title                  # DB
    project_title_fs = team.project_title.replace(" ", "_")  # Folder

    print("[DEBUG] Team title (DB):", team_title_db)
    print("[DEBUG] Project title (FS):", project_title_fs)

    # =================================================
    # 📁 Project folder path
    # =================================================
    output_dir = os.path.join(
        settings.BASE_DIR,
        "project_docs",
        project_title_fs
    )
    os.makedirs(output_dir, exist_ok=True)

    print(f"[DEBUG] Output directory: {output_dir}")

    # =================================================
    # 📄 Expected files
    # =================================================
    expected_files = {
        "ppt": f"{project_title_fs}_PPT",
        "pdf": f"{project_title_fs}_Report",
        "abstract": f"{project_title_fs}_Abstract"
    }

    uploaded_files = {}

    # =================================================
    # 🔎 Detect already uploaded files
    # =================================================
    for key, base_name in expected_files.items():
        for ext in [".ppt", ".pptx", ".pdf"]:
            file_path = os.path.join(output_dir, base_name + ext)
            if os.path.exists(file_path):
                uploaded_files[key] = {
                    "name": os.path.basename(file_path),
                    "path": file_path
                }
                print(f"[DEBUG] Found uploaded file: {file_path}")

    # =================================================
    # 📩 POST → Upload missing files
    # =================================================
    if request.method == "POST":
        ppt_file = request.FILES.get("pptFile")
        pdf_file = request.FILES.get("pdfFile")
        abstract_file = request.FILES.get("abstractFile")

        saved_files = {}

        def save_file(file_obj, prefix):
            ext = os.path.splitext(file_obj.name)[1]
            filename = prefix + ext
            file_path = os.path.join(output_dir, filename)
            with open(file_path, "wb+") as dest:
                for chunk in file_obj.chunks():
                    dest.write(chunk)
            print(f"[DEBUG] Saved file: {file_path}")
            return file_path

        if ppt_file:
            saved_files["ppt"] = save_file(ppt_file, expected_files["ppt"])
        if pdf_file:
            saved_files["pdf"] = save_file(pdf_file, expected_files["pdf"])
        if abstract_file:
            saved_files["abstract"] = save_file(abstract_file, expected_files["abstract"])

        return JsonResponse({
            "status": "success",
            "message": "Files uploaded successfully",
            "files": saved_files
        })

    # =================================================
    # 📝 GET → Fetch mentor zeroth review remarks
    # =================================================
    print("🔍 Fetching Zeroth Review remarks for student")

    remarks_qs = ZerothReviewRemark.objects.filter(
        team_name=team_title_db
    ).order_by("created_at")

    print("📝 Remarks found:", remarks_qs.count())
    for r in remarks_qs:
        print(" -", r.heading, "|", r.remark[:40], "| color:", r.color)

    remarks_data = [
        {
            "heading": r.heading,
            "remark": r.remark,
            "color": r.color,
            "created_at": r.created_at
        }
        for r in remarks_qs
    ]

    # =================================================
    # 🌐 Highlighted Abstract HTML
    # =================================================
# Determine highlighted HTML file (mentor highlighted)
    html_dir = os.path.join(output_dir, "html")
    highlighted_html_file = None

    if os.path.exists(html_dir):
        html_files = [f for f in os.listdir(html_dir) if f.lower().endswith(".html")]
        if html_files:
            highlighted_html_file = html_files[0]

    highlighted_html_url = (
        f"/project_docs/{project_title_fs}/html/{highlighted_html_file}"
        if highlighted_html_file else None
    )


    return render(
        request,
        "student/review/zero_ma.html",
        {
            "student_name": student_name,
            "username": username,
            "uploaded_files": uploaded_files,
            "remarks": remarks_data,
            "highlighted_html_url": highlighted_html_url,
        }
    )


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from allocation.models import ZerothReviewRemark, AllocationResult

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def save_zeroth_remark(request):
    print("🔥 save_zeroth_remark CALLED")

    if request.method != "POST":
        return JsonResponse({"status": "fail", "message": "Invalid request"})

    mentor_name = request.session.get("mentor_name")
    print("Mentor:", mentor_name)

    allocation = AllocationResult.objects.filter(
        mentor_name=mentor_name
    ).first()

    if not allocation:
        print("❌ No allocation found")
        return JsonResponse({"status": "fail", "message": "No team allocated"})

    team_name = allocation.team_name
    print("Team:", team_name)

    try:
        data = json.loads(request.body)
        remarks = data.get("remarks", [])
        print("Remarks count:", len(remarks))
    except Exception as e:
        print("❌ JSON error:", e)
        return JsonResponse({"status": "fail", "message": "Invalid JSON"})

    for r in remarks:
        heading = (r.get("heading") or "").strip()
        remark = (r.get("remark") or "").strip()
        color = r.get("color") or "#ffe066"

        if not heading or not remark:
            continue

        print("Saving remark:", heading)

        obj, created = ZerothReviewRemark.objects.update_or_create(
            team_name=team_name,
            mentor_name=mentor_name,
            heading=heading,
            defaults={
                "remark": remark,
                "color": color,
            }
        )

        if created:
            print("🆕 Inserted:", heading)
        else:
            print("🔁 Updated (no duplicate):", heading)

    print("✅ Remarks saved successfully")
    return JsonResponse({"status": "success"})


def clean_text(text):
    return re.sub(r'\(.*?\)', '', text).strip().lower()


@csrf_exempt
def save_evaluation(request):
    if request.method != "POST":
        return JsonResponse({"status": "fail", "message": "Invalid request method"}, status=400)

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # {"team_member-Name": ["Criteria-Mark", ...]}

        if not team_name or not evaluations:
            return JsonResponse({"status": "fail", "message": "Missing team name or evaluations"}, status=400)

        # --- File paths ---
        template_path = os.path.join(settings.BASE_DIR, 'allocation', 'static', 'zeroth_review_mark.docx')
        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{team_name}_ZerothReview.docx")

        # --- Load existing doc ---
        if os.path.exists(output_path):
            doc = Document(output_path)
        else:
            if not os.path.exists(template_path):
                return JsonResponse({"status": "error", "message": f"Template not found: {template_path}"}, status=500)
            doc = Document(template_path)

        # --- Insert team name ---
        for para in doc.paragraphs:
            if "project title" in para.text.lower():
                para.text = f"Project Title: {team_name}"
                break

        # --- Locate team members table ---
        members_table = None
        for t in doc.tables:
            if "team members" in clean_text(t.cell(0, 0).text):
                members_table = t
                break
        if not members_table:
            return JsonResponse({"status": "error", "message": "Team Members table not found"}, status=500)

        # --- Add new members if not existing ---
        existing_names = []
        for r in members_table.rows[1:]:
            if len(r.cells) > 3 and r.cells[3].text.strip():
                existing_names.append(r.cells[3].text.strip())

        # 🟢 FIXED: start numbering from 1, not 0
        current_index = len(existing_names)
        for member_name in evaluations.keys():
            clean_name = member_name.replace("team_member-", "").strip()
            if clean_name in existing_names:
                continue

            empty_row = next((r for r in members_table.rows[1:] if not r.cells[3].text.strip()), None)
            if not empty_row:
                empty_row = members_table.add_row()
                for c in empty_row.cells:
                    c.text = ""

            empty_row.cells[0].text = str(current_index)
            empty_row.cells[1].text = "-"
            empty_row.cells[2].text = "-"
            empty_row.cells[3].text = clean_name
            existing_names.append(clean_name)
            current_index += 1  # ✅ ensures new member gets next S.No

        # --- Locate marks table ---
        marks_table = None
        for t in doc.tables:
            for row in t.rows:
                if any(k in clean_text(row.cells[0].text) for k in
                       ["project concept", "literature review", "relevance", "project planning", "methodology", "presentation"]):
                    marks_table = t
                    break
            if marks_table:
                break
        if not marks_table:
            return JsonResponse({"status": "error", "message": "Marks table not found"}, status=500)

        # --- Build criteria row map ---
        criteria_map = {}
        total_row = None
        for i, row in enumerate(marks_table.rows):
            t0 = clean_text(row.cells[0].text)
            if "total" in t0:
                total_row = i
            for key in ["project concept", "literature review", "relevance",
                        "project planning", "methodology", "presentation"]:
                if key in t0:
                    criteria_map[key] = i

        if total_row is None:
            return JsonResponse({"status": "error", "message": "Total row not found"}, status=500)

        # --- Map team member names → S.No from members_table ---
        member_to_sno = {}
        for r in members_table.rows[1:]:
            if len(r.cells) > 3 and r.cells[3].text.strip():
                name = r.cells[3].text.strip()
                sno = r.cells[0].text.strip()
                member_to_sno[name.lower()] = sno

        print("[DEBUG] Member → S.No map:", member_to_sno)

        # --- Insert marks ---
        for member_name, marks_list in evaluations.items():
            name = member_name.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(name)
            if not sno:
                print(f"[DEBUG] No S.No for {name}")
                continue

            # 🟢 FIXED: ensures data goes into correct “1/2/3/4” column
            print(sno)
            col = 3 + int(sno)

            if col >= len(marks_table.rows[0].cells):
                print(f"[DEBUG] Column out of range for {name}")
                continue

            marks_dict = {}
            for item in marks_list:
                if '-' in item:
                    crit, val = item.rsplit('-', 1)
                    try:
                        marks_dict[crit.strip()] = int(val.lstrip('0') or '0')
                    except:
                        pass

            total = 0
            print(f"[DEBUG] Filling marks for {name} (S.No {sno}) → column {col}")

            for crit, mark in marks_dict.items():
                ckey = clean_text(crit)
                row_index = next((criteria_map[k] for k in criteria_map if k in ckey or ckey in k), None)
                if row_index is not None:
                    marks_table.rows[row_index].cells[col].text = str(mark)
                    total += mark
                    print(f"[DEBUG] {crit}: {mark} in row {row_index}, col {col}")

            marks_table.rows[total_row].cells[col].text = str(total)
            print(f"[DEBUG] TOTAL {total} for {name}")

        # --- Safe save ---
        try:
            doc.save(output_path)
        except PermissionError:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            alt = os.path.join(output_dir, f"{team_name}_ZerothReview_{timestamp}.docx")
            doc.save(alt)
            output_path = alt

        return JsonResponse({
            "status": "success",
            "message": "Marks inserted successfully",
            "file_path": output_path
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status": "error", "message": str(e)}, status=500)



from django.http import FileResponse, JsonResponse # type: ignore
import os
from django.conf import settings
from docx2pdf import convert

def download_docx(request, team_name):
    """Download existing DOCX file."""
    file_path = os.path.join(settings.BASE_DIR, "generated_docs", f"{team_name}_ZerothReview.docx")
    
    if not os.path.exists(file_path):
        return JsonResponse({"error": "DOCX file not found"}, status=404)
    
    return FileResponse(open(file_path, "rb"), as_attachment=True, filename=f"{team_name}_ZerothReview.docx")


import os
import pdfkit
from django.http import FileResponse, JsonResponse
from django.conf import settings
from docx import Document
from tempfile import NamedTemporaryFile

def download_pdf(request, team_name):
    docx_path = os.path.join(settings.BASE_DIR, "generated_docs", f"{team_name}_ZerothReview.docx")
    pdf_path = os.path.join(settings.BASE_DIR, "generated_docs", f"{team_name}_ZerothReview.pdf")

    if not os.path.exists(docx_path):
        return JsonResponse({"error": "DOCX file not found"}, status=404)

    # Convert DOCX text → HTML → PDF
    document = Document(docx_path)
    html_content = "<h2>{}</h2>".format(team_name)
    for para in document.paragraphs:
        html_content += f"<p>{para.text}</p>"

    # Save temporary HTML
    with NamedTemporaryFile(delete=False, suffix=".html") as tmp_html:
        tmp_html.write(html_content.encode("utf-8"))
        tmp_html_path = tmp_html.name

    pdfkit.from_file(tmp_html_path, pdf_path)

    return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename=f"{team_name}_ZerothReview.pdf")


import os, json, time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from docx import Document

def clean_text(text):
    return text.strip().lower()

@csrf_exempt
def save_evaluation_review1(request):
    if request.method != "POST":
        return JsonResponse({"status": "fail", "message": "Invalid request method"}, status=400)

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # {"member_name": [marks list]}
        print(evaluations)
        if not team_name or not evaluations:
            return JsonResponse({"status": "fail", "message": "Missing team name or evaluations"}, status=400)

        # --- File paths ---
        template_path = os.path.join(settings.BASE_DIR, 'allocation', 'static', 'first_review_mark.docx')
        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{team_name}_Review1.docx")

        # --- Load or create doc ---
        doc = Document(output_path) if os.path.exists(output_path) else Document(template_path)

        # --- Update title ---
        for para in doc.paragraphs:
            if "review 1 evaluation" in para.text.lower():
                para.text = f"Review 1 Evaluation - {team_name}"
                break

        # --- Locate members table ---
        members_table = doc.tables[0]  # first table assumed for TEAM MEMBERS

        # --- Add/update members ---
        start_row = 2  # 0-indexed: row 0=S.NO header, row1=Student Name header
        for idx, member_name in enumerate(evaluations.keys()):
            clean_name = member_name.replace("team_member-", "").strip()
            row_index = start_row + idx
            if row_index >= len(members_table.rows):
                members_table.add_row()
            members_table.rows[row_index].cells[3].text = clean_name

        # --- Map member name → S.NO ---
        member_to_sno = {}
        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                name = r.cells[3].text.strip().lower()
                sno = r.cells[0].text.strip()
                member_to_sno[name] = sno

        # --- Locate marks table ---
        marks_table = doc.tables[1]

        # --- Detect TOTAL row ---
        total_row = None
        for i, row in enumerate(marks_table.rows):
            if "total" in row.cells[0].text.lower():
                total_row = i
                break
        if total_row is None:
            total_row = len(marks_table.rows) - 1  # fallback

        # --- Locate S.NO row to detect columns ---
        sno_row_idx = None
        sno_col_map = {}
        for i, row in enumerate(marks_table.rows):
            for idx, cell in enumerate(row.cells):
                if cell.text.strip().isdigit():
                    sno_col_map[cell.text.strip()] = idx
                    sno_row_idx = i
            if sno_col_map:
                break

        # --- Insert marks using S.NO mapping ---
        for member_name, marks_list in evaluations.items():
            clean_name = member_name.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(clean_name)
            if not sno:
                continue
            col_idx = sno_col_map.get(sno)
            if col_idx is None:
                continue

            total = 0
            row_idx = sno_row_idx + 1  # start filling just below S.NO row
            for mark in marks_list:
                if row_idx >= total_row:
                    break
                try:
                    marks_table.rows[row_idx].cells[col_idx].text = str(mark)
                    total += int(mark)
                except:
                    pass
                row_idx += 1

            # update TOTAL
            marks_table.rows[total_row].cells[col_idx].text = str(total)

        # --- Save document ---
        try:
            doc.save(output_path)
        except PermissionError:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            alt = os.path.join(output_dir, f"{team_name}_Review1_{timestamp}.docx")
            doc.save(alt)
            output_path = alt

        return JsonResponse({
            "status": "success",
            "message": "Marks inserted successfully",
            "file_path": output_path
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

