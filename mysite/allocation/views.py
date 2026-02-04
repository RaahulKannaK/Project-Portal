
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
from .models import AnnouncementStatus, Stu_Login

def student_dashboard(request):
    # ===============================
    # SESSION CHECK
    # ===============================
    student_id = request.session.get("student_id")
    username = request.session.get("username")
    student_name = request.session.get("student_name")

    if not student_id:
        return redirect("login")

    password_updated = False
    password_error = None

    # ===============================
    # PASSWORD RESET HANDLER
    # ===============================
    if request.method == "POST" and request.POST.get("action") == "reset_password":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not new_password or not confirm_password:
            password_error = "Both fields are required."
        elif new_password != confirm_password:
            password_error = "Passwords do not match."
        else:
            try:
                user = Stu_Login.objects.get(username=username)
                user.password = new_password  # ⚠️ plain text as per your current setup
                user.save()
                password_updated = True
            except Stu_Login.DoesNotExist:
                password_error = "User not found."

    # ===============================
    # FETCH ANNOUNCEMENTS FOR STUDENT
    # ===============================
    announcements = AnnouncementStatus.objects.filter(
        receiver_role="student",
        receiver_id=student_id
    ).select_related("announcement").order_by("-announcement__created_at")

    # AUTO MARK AS SEEN
    announcements.filter(seen_at__isnull=True).update(
        seen_at=timezone.now()
    )

    # ===============================
    # RENDER DASHBOARD
    # ===============================
    return render(request, "student/stu_dash.html", {
        "student_name": student_name,
        "username": username,
        "student_id": student_id,
        "announcements": announcements,
        "password_updated": password_updated,
        "password_error": password_error,
    })


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

from django.shortcuts import render
from allocation.models import AllocationResult, Team, ProjectDocument, ZerothReviewRemark

def mentor_dashboard(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")

    if not mentor_name:
        return redirect("mentor_login")

    allocations = AllocationResult.objects.filter(mentor_name=mentor_name)

    team_details = []

    for alloc in allocations:
        team = Team.objects.filter(project_title__iexact=alloc.team_name).first()
        if not team:
            continue

        # ---- Documents ----
        documents = ProjectDocument.objects.filter(team_name=team.project_title)

        doc_map = {}
        for d in documents:
            doc_map.setdefault(d.review_stage, {})
            doc_map[d.review_stage][d.doc_type] = d

        # ---- Zeroth Review Remarks ----
        remarks = ZerothReviewRemark.objects.filter(
            team_name=team.project_title,
            mentor_name=mentor_name
        )
        remark_map = {r.heading: r for r in remarks}

        members = list(zip(
            team.member_names.split(","),
            team.members.split(",")
        ))

        team_details.append({
            "project_title": team.project_title,
            "domain": team.domain,
            "members": members,
            "documents": doc_map,
            "remarks": remark_map,
        })

    return render(request, "mentor/men_dash.html", {
        "mentor_name": mentor_name,
        "username": username,
        "team_details": team_details,
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
    team_members = []
    team_name = None

    # Get the latest allocation for this mentor
    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).order_by('-allocated_at').first()
    if allocation:
        team_name = allocation.team_name

        # Fetch team using project_title instead of team_name
        team = Team.objects.filter(project_title=team_name).first()
        if team and team.member_names:
            team_members = team.member_names.split(",")

    return render(request, "mentor/review_men/2_men.html", {
        "mentor_name": mentor_name,
        "username": username,
        "team_name": team_name,
        "team_members": team_members,
    })


def three_men(request):
    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")
    team_members = []
    team_name = None

    # Get the latest allocation for this mentor
    allocation = AllocationResult.objects.filter(mentor_name=mentor_name).order_by('-allocated_at').first()
    if allocation:
        team_name = allocation.team_name

        # Fetch team using project_title instead of team_name
        team = Team.objects.filter(project_title=team_name).first()
        if team and team.member_names:
            team_members = team.member_names.split(",")

    return render(request, "mentor/review_men/3_men.html", {
        "mentor_name": mentor_name,
        "username": username,
        "team_name": team_name,
        "team_members": team_members,
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
    Serve PDF from Cloudinary via direct URL (iframe-safe)
    """
    from allocation.models import TeamDocument  # nee create panna model (next step)

    doc = TeamDocument.objects.filter(
        team_name=team_name,
        doc_type=pdf_type
    ).first()

    if not doc or not doc.file_url:
        raise Http404("PDF not found")

    return redirect(doc.file_url)


import os
import re
import subprocess
import pdfplumber

from django.conf import settings
from django.shortcuts import render
from .models import AllocationResult


import os
import re
import json
import tempfile
import subprocess
import requests
import pdfplumber

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import transaction, IntegrityError

from .models import AllocationResult, ZerothReviewRemark, ProjectFile

# --------------------------------------------------
# 🔍 HEADING VALIDATION (STRICT)
# --------------------------------------------------
def is_valid_heading(text):
    text = text.strip()
    if text.startswith(("-", "•")): return False
    if re.match(r"^\d+[\.\)]", text): return False
    if len(text) > 70: return False
    if text.endswith(".") or text.endswith(":"): return False
    if any(word.islower() for word in text.split()[1:]): return False
    return any(word[0].isupper() for word in text.split() if word)

# --------------------------------------------------
# 🧠 EARLY PAGE HEADING DETECTOR
# --------------------------------------------------
def looks_like_early_heading(text, top, page_no):
    text = text.strip()
    early_keywords = {"abstract", "introduction", "problem statement", "background", "motivation"}
    if text.lower() in early_keywords: return True
    if text.endswith(":"): return False
    if page_no <= 2 and len(text.split()) <= 4 and text[0].isupper() and not text.endswith("."):
        return True
    return False

import os
import re
import subprocess
import json
import requests
from bs4 import BeautifulSoup

from django.conf import settings
from django.db import transaction, IntegrityError
from django.shortcuts import render
from django.http import JsonResponse

from .models import AllocationResult, ProjectFile, ZerothReviewRemark  # your existing functions


import os
import re
import json
import shutil
import subprocess
import requests

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction, IntegrityError

from .models import AllocationResult, ZerothReviewRemark, ProjectFile

# -----------------------------
# Heading validators
# -----------------------------
def is_valid_heading(text):
    text = text.strip()
    if text.startswith(("-", "•")): return False
    if re.match(r"^\d+[\.\)]", text): return False
    if len(text) > 70: return False
    if text.endswith(".") or text.endswith(":"): return False
    if any(word.islower() for word in text.split()[1:]): return False
    return any(word[0].isupper() for word in text.split() if word)

def looks_like_early_heading(text, top=0, page_no=1):
    text = text.strip()
    early_keywords = {"abstract", "introduction", "problem statement", "background", "motivation"}
    if text.lower() in early_keywords: return True
    if page_no <= 2 and len(text.split()) <= 4 and text[0].isupper() and not text.endswith("."):
        return True
    return False

# -----------------------------
# Zero Review View
# -----------------------------
def zero_review(request):
    print("\n🟢 zero_review CALLED")

    mentor_name = request.session.get("mentor_name")
    username = request.session.get("username")

    print("mentor_name:", mentor_name)
    print("username:", username)
    print("method:", request.method)

    # =====================================================
    # POST → SAVE ZEROTH REVIEW REMARKS
    # =====================================================
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            remarks = data.get("remarks", [])
            print("Incoming remarks:", len(remarks))

            allocation = AllocationResult.objects.filter(
                mentor_name=mentor_name
            ).first()

            if not allocation:
                return JsonResponse({"status": "fail", "message": "Team not found"}, status=404)

            team_name = allocation.team_name
            inserted = 0
            updated = 0

            for r in remarks:
                heading = (r.get("heading") or "").strip()
                remark = (r.get("remark") or "").strip()
                color = r.get("color") or "#ffe066"

                if not heading or not remark:
                    continue

                obj, created = ZerothReviewRemark.objects.update_or_create(
                    team_name=team_name,
                    mentor_name=mentor_name,
                    heading=heading,
                    defaults={
                        "remark": remark,
                        "color": color
                    }
                )

                if created:
                    inserted += 1
                else:
                    updated += 1

            return JsonResponse({
                "status": "success",
                "inserted": inserted,
                "updated": updated
            })

        except Exception as e:
            print("❌ POST ERROR:", e)
            return JsonResponse({"status": "fail", "message": str(e)}, status=500)

    # =====================================================
    # GET → DISPLAY PAGE
    # =====================================================
    allocation = AllocationResult.objects.filter(
        mentor_name=mentor_name
    ).first()

    if not allocation:
        return render(request, "mentor/review_men/men_doc/zero_paper/zero_review.html")

    team_name = allocation.team_name
    folder_name = team_name.replace(" ", "_")

    print("Team:", team_name)

    # =====================================================
    # 🔥 LOAD SAVED REMARKS
    # =====================================================
    saved_remarks = ZerothReviewRemark.objects.filter(
        team_name=team_name,
        mentor_name=mentor_name
    ).order_by("id")

    print("🔥 Loaded remarks:", saved_remarks.count())
    for r in saved_remarks:
        print(" ->", r.heading)

    # =====================================================
    # ABSTRACT FILE FROM CLOUDINARY
    # =====================================================
    project_file = ProjectFile.objects.filter(
        team_name=team_name,
        file_type="abstract"
    ).first()

    if not project_file:
        return render(request, "mentor/review_men/men_doc/zero_paper/zero_review.html", {
            "zero_review": False
        })

    cloud_url = project_file.cloudinary_url

    temp_dir = os.path.join(settings.MEDIA_ROOT, "temp_html", folder_name)
    os.makedirs(temp_dir, exist_ok=True)

    pdf_name = f"{folder_name}_Abstract.pdf"
    html_name = f"{folder_name}_Abstract.html"

    pdf_path = os.path.join(temp_dir, pdf_name)
    html_path = os.path.join(temp_dir, html_name)

    # =====================================================
    # DOWNLOAD PDF
    # =====================================================
    if not os.path.exists(pdf_path):
        try:
            r = requests.get(cloud_url, timeout=20)
            r.raise_for_status()
            with open(pdf_path, "wb") as f:
                f.write(r.content)
            print("✔ PDF downloaded")
        except Exception as e:
            print("❌ PDF DOWNLOAD ERROR:", e)
            return render(request, "mentor/review_men/men_doc/zero_paper/zero_review.html")

    # =====================================================
    # PDF → HTML
    # =====================================================
    if not os.path.exists(html_path):
        try:
            subprocess.run(
                [
                    "docker", "run", "--rm",
                    "-v", f"{temp_dir}:/pdf",
                    "pdf2html_local",
                    pdf_name,
                    "--dest-dir", "/pdf"
                ],
                check=True
            )
            print("✔ PDF converted to HTML")
        except Exception as e:
            print("❌ PDF→HTML ERROR:", e)

    # =====================================================
    # READ HTML CONTENT
    # =====================================================
    html_content = ""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except Exception as e:
        print("❌ HTML READ ERROR:", e)

    # =====================================================
    # HEADING EXTRACTION
    # =====================================================
    main_heading_lines = []
    sub_headings = []

    lines = re.findall(r'>([^<]{2,120})<', html_content)

    for line in lines:
        text = line.strip()
        if not text:
            continue

        if is_valid_heading(text):
            if not main_heading_lines:
                main_heading_lines.append(text)
            elif text not in sub_headings:
                sub_headings.append(text)
        elif looks_like_early_heading(text):
            if text not in sub_headings:
                sub_headings.append(text)

    main_heading = " ".join(main_heading_lines)

    # =====================================================
    # FINAL RENDER
    # =====================================================
    return render(
        request,
        "mentor/review_men/men_doc/zero_paper/zero_review.html",
        {
            "mentor_name": mentor_name,
            "username": username,
            "team_name": team_name,
            "main_heading": main_heading,
            "sub_headings": sub_headings,
            "html_content": html_content,
            "saved_remarks": saved_remarks,   # 🔥 IMPORTANT
            "zero_review": True
        }
    )


from django.http import FileResponse, Http404

def serve_temp_html(request, team, filename):
    print(f"[DEBUG] serve_temp_html → team={team}, file={filename}")

    html_path = os.path.join(
        settings.MEDIA_ROOT,
        "temp_html",
        team,
        filename
    )

    print(f"[DEBUG] Absolute HTML path: {html_path}")

    if not os.path.exists(html_path):
        print("[ERROR] HTML file not found")
        raise Http404("HTML file not found")

    return FileResponse(
        open(html_path, "rb"),
        content_type="text/html"
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
    team_name = None

    allocation = AllocationResult.objects.filter(
        mentor_name=mentor_name
    ).first()

    if allocation:
        team_name = allocation.team_name

        # ✅ CLOUDINARY PPT URL (NO LOCAL STORAGE)
        ppt_path = allocation.zeroth_ppt_url

        if ppt_path:
            print(f"[DEBUG] Cloudinary PPT URL found: {ppt_path}")
        else:
            print("[DEBUG] PPT URL not available in Cloudinary")

    else:
        print(
            f"[DEBUG] No allocated team found for mentor '{mentor_name}'"
        )

    return render(
        request,
        "mentor/review_men/men_doc/zero_paper/zero_ppt.html",
        {
            "mentor_name": mentor_name,
            "username": username,
            "ppt_path": ppt_path,   # 👈 Cloudinary URL
            "team_name": team_name,
        }
    )


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


def two_ma(request, team_name):
    team_members = []
    
    # Fetch team object using project_title
    team = Team.objects.filter(project_title=team_name).first()
    if team and team.member_names:
        # Convert comma-separated string to list
        team_members = team.member_names.split(",")

    # Render the Review 1 (mentor assessment) page for a specific team
    return render(request, 'mentor/review_men/men_ma/two_ma.html', {
        'team_name': team_name,
        'team_members': team_members
    })

def three_ma(request, team_name):
    team_members = []
    
    # Fetch team object using project_title
    team = Team.objects.filter(project_title=team_name).first()
    if team and team.member_names:
        # Convert comma-separated string to list
        team_members = team.member_names.split(",")

    # Render the Review 3 mentor assessment page
    return render(request, 'mentor/review_men/men_ma/three_ma.html', {
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
import cloudinary.uploader
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ProjectFile



# ======================================================
# 🔹 REVIEW 1 — STUDENT
# ======================================================
def one_stu(request):
    student_name = request.session.get("student_name")
    username = request.session.get("username")

    if not student_name:
        return redirect("login")

    team = Team.objects.filter(
        member_names__icontains=student_name
    ).first()

    if not team:
        return render(request, "student/review/1_stu.html", {
            "error": "Team not found"
        })

    # 🔁 Already uploaded file
    existing = ReviewFile.objects.filter(
        team_name=team.project_title,
        review_type=1
    ).first()

    if request.method == "POST":
        ppt_file = request.FILES.get("pptFile")

        if not ppt_file:
            return JsonResponse({"status": "fail", "message": "No PPT uploaded"})

        upload = cloudinary.uploader.upload(
            ppt_file,
            resource_type="raw",
            folder="review1_ppt"
        )

        ReviewFile.objects.update_or_create(
            team_name=team.project_title,
            review_type=1,
            defaults={"ppt_url": upload["secure_url"]}
        )

        return JsonResponse({
            "status": "success",
            "ppt_url": upload["secure_url"]
        })

    return render(request, "student/review/1_stu.html", {
        "student_name": student_name,
        "username": username,
        "ppt_url": existing.ppt_url if existing else None
    })


# ======================================================
# 🔹 REVIEW 2 — STUDENT
# ======================================================
def two_stu(request):
    student_name = request.session.get("student_name")
    username = request.session.get("username")

    if not student_name:
        return redirect("login")

    team = Team.objects.filter(
        member_names__icontains=student_name
    ).first()

    if not team:
        return render(request, "student/review/2_stu.html", {
            "error": "Team not found"
        })

    existing = ReviewFile.objects.filter(
        team_name=team.project_title,
        review_type=2
    ).first()

    if request.method == "POST":
        ppt_file = request.FILES.get("pptFile")

        if not ppt_file:
            return JsonResponse({"status": "fail", "message": "No PPT uploaded"})

        upload = cloudinary.uploader.upload(
            ppt_file,
            resource_type="raw",
            folder="review2_ppt"
        )

        ReviewFile.objects.update_or_create(
            team_name=team.project_title,
            review_type=2,
            defaults={"ppt_url": upload["secure_url"]}
        )

        return JsonResponse({
            "status": "success",
            "ppt_url": upload["secure_url"]
        })

    return render(request, "student/review/2_stu.html", {
        "student_name": student_name,
        "username": username,
        "ppt_url": existing.ppt_url if existing else None
    })


# ======================================================
# 🔹 REVIEW 3 — STUDENT
# ======================================================
def three_stu(request):
    student_name = request.session.get("student_name")
    username = request.session.get("username")

    if not student_name:
        return redirect("login")

    team = Team.objects.filter(
        member_names__icontains=student_name
    ).first()

    if not team:
        return render(request, "student/review/3_stu.html", {
            "error": "Team not found"
        })

    existing = ReviewFile.objects.filter(
        team_name=team.project_title,
        review_type=3
    ).first()

    if request.method == "POST":
        ppt_file = request.FILES.get("pptFile")

        if not ppt_file:
            return JsonResponse({"status": "fail", "message": "No PPT uploaded"})

        upload = cloudinary.uploader.upload(
            ppt_file,
            resource_type="raw",
            folder="review3_ppt"
        )

        ReviewFile.objects.update_or_create(
            team_name=team.project_title,
            review_type=3,
            defaults={"ppt_url": upload["secure_url"]}
        )

        return JsonResponse({
            "status": "success",
            "ppt_url": upload["secure_url"]
        })

    return render(request, "student/review/3_stu.html", {
        "student_name": student_name,
        "username": username,
        "ppt_url": existing.ppt_url if existing else None
    })


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



import io
import json
import cloudinary.uploader

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import transaction

from allocation.models import ZerothReviewRemark
from allocation.models import ProjectFile, Team


# ============================================
# 🔹 Helper Function: Upload to Cloudinary
# ============================================
from django.shortcuts import render, redirect
from django.http import JsonResponse
from allocation.models import Team, ProjectFile, ZerothReviewRemark
import cloudinary
import json

# -----------------------------
# Helper: Upload to Cloudinary
# -----------------------------
def upload_to_cloudinary(file_obj, file_type, folder_name):
    try:
        print(f"DEBUG: Uploading {file_type} to Cloudinary...")
        result = cloudinary.uploader.upload(
            file_obj,
            resource_type="auto",       # Supports PDF, PPT, etc.
            folder=f"project_portal/{folder_name}",
            public_id=f"{folder_name}_{file_type}",
            overwrite=True,
            use_filename=True,
            unique_filename=False,
            access_mode="public"        # Ensure public access
        )
        file_url = result.get("secure_url")
        print(f"DEBUG: Uploaded {file_type} URL → {file_url}")
        return file_url
    except Exception as e:
        print(f"❌ Cloudinary upload failed for {file_type}: {e}")
        return None


# -----------------------------
# View: Student Upload (Zero Review)
# -----------------------------
def zero_ma1(request):
    # ---------------------------
    # 1️⃣ Get Student Session
    # ---------------------------
    student_name = request.session.get("student_name")
    username = request.session.get("username")
    print("DEBUG: Student session →", student_name, username)

    if not student_name:
        return redirect("login")

    # ---------------------------
    # 2️⃣ Find Student Team
    # ---------------------------
    team = Team.objects.filter(member_names__icontains=student_name).first()
    if not team:
        return render(request, "student/review/zero_ma.html", {
            "student_name": student_name,
            "username": username,
            "error": "Team not found"
        })

    team_title = team.project_title
    folder_name = team_title.replace(" ", "_")
    print("DEBUG: Found team →", team_title)

    # ---------------------------
    # 3️⃣ Handle POST → Upload Files
    # ---------------------------
    if request.method == "POST":
        ppt_file = request.FILES.get("pptFile")
        pdf_file = request.FILES.get("pdfFile")
        abstract_file = request.FILES.get("abstractFile")
        print("DEBUG: Files received →", ppt_file, pdf_file, abstract_file)

        uploaded = {}

        if ppt_file:
            uploaded["ppt"] = upload_to_cloudinary(ppt_file, "PPT", folder_name)

        if pdf_file:
            uploaded["pdf"] = upload_to_cloudinary(pdf_file, "Report", folder_name)

        if abstract_file:
            uploaded["abstract"] = upload_to_cloudinary(abstract_file, "Abstract", folder_name)

        print("DEBUG: Uploaded files dict →", uploaded)

        # ---------------------------
        # 4️⃣ Update ProjectFile Table (use team_name instead of ForeignKey)
        # ---------------------------
        for ftype, url in uploaded.items():
            if url:
                obj, created = ProjectFile.objects.update_or_create(
                    team_name=team_title,   # <-- store team_name as string
                    review_type="zero",
                    file_type=ftype,
                    defaults={"cloudinary_url": url}
                )
                print(f"DEBUG: ProjectFile {'created' if created else 'updated'} → {ftype}: {url}")

        return JsonResponse({
            "status": "success",
            "message": "Files uploaded to Cloudinary",
            "files": uploaded
        })

    # ---------------------------
    # 5️⃣ GET → Fetch already uploaded files
    # ---------------------------
    uploaded_files = {}
    files_qs = ProjectFile.objects.filter(team_name=team_title, review_type="zero")
    for f in files_qs:
        uploaded_files[f.file_type] = f.cloudinary_url
    print("DEBUG: Uploaded files fetched →", uploaded_files)

    # ---------------------------
    # 6️⃣ Get Zeroth Review Remarks
    # ---------------------------
    remarks_qs = ZerothReviewRemark.objects.filter(team_name=team_title).order_by("created_at")
    remarks_data = [
        {
            "heading": r.heading,
            "remark": r.remark,
            "color": r.color,
            "created_at": r.created_at
        }
        for r in remarks_qs
    ]
    print("DEBUG: Remarks fetched →", len(remarks_data))

    # ---------------------------
    # 7️⃣ Final Render
    # ---------------------------
    return render(request, "student/review/zero_ma.html", {
        "student_name": student_name,
        "username": username,
        "team_name": team_title,
        "uploaded_files": uploaded_files,
        "remarks": remarks_data,
    })

# ============================================
# 🔹 Student Zero Review File Upload View
# ============================================


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
    """
    📝 Save Zeroth Review Evaluation Marks into DOCX
    """

    if request.method != "POST":
        return JsonResponse(
            {"status": "fail", "message": "Invalid request method"},
            status=400
        )

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # dict

        if not team_name or not evaluations:
            return JsonResponse(
                {"status": "fail", "message": "Missing team name or evaluations"},
                status=400
            )

        # -------------------------------------------------
        # Safe team name (filesystem)
        # -------------------------------------------------
        team_name_fs = team_name.replace(" ", "_")

        # -------------------------------------------------
        # Paths
        # -------------------------------------------------
        template_path = os.path.join(
            settings.BASE_DIR,
            "allocation",
            "static",
            "zeroth_review_mark.docx"
        )

        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(
            output_dir,
            f"{team_name_fs}_ZerothReview.docx"
        )

        print("[DEBUG] Output DOCX:", output_path)

        # -------------------------------------------------
        # Load existing doc OR template
        # -------------------------------------------------
        if os.path.exists(output_path):
            doc = Document(output_path)
        else:
            if not os.path.exists(template_path):
                return JsonResponse(
                    {
                        "status": "error",
                        "message": f"Template not found: {template_path}"
                    },
                    status=500
                )
            doc = Document(template_path)

        # -------------------------------------------------
        # Insert project title
        # -------------------------------------------------
        for para in doc.paragraphs:
            if "project title" in para.text.lower():
                para.text = f"Project Title: {team_name}"
                break

        # -------------------------------------------------
        # Locate Team Members table
        # -------------------------------------------------
        members_table = None
        for t in doc.tables:
            if "team members" in clean_text(t.cell(0, 0).text):
                members_table = t
                break

        if not members_table:
            return JsonResponse(
                {"status": "error", "message": "Team Members table not found"},
                status=500
            )

        # -------------------------------------------------
        # Existing members
        # -------------------------------------------------
        existing_names = []
        for r in members_table.rows[1:]:
            if len(r.cells) > 3 and r.cells[3].text.strip():
                existing_names.append(r.cells[3].text.strip())

        current_index = len(existing_names) + 1  # ✅ start from next S.No

        for member_key in evaluations.keys():
            clean_name = member_key.replace("team_member-", "").strip()
            if clean_name in existing_names:
                continue

            empty_row = next(
                (r for r in members_table.rows[1:] if not r.cells[3].text.strip()),
                None
            )

            if not empty_row:
                empty_row = members_table.add_row()
                for c in empty_row.cells:
                    c.text = ""

            empty_row.cells[0].text = str(current_index)
            empty_row.cells[1].text = "-"
            empty_row.cells[2].text = "-"
            empty_row.cells[3].text = clean_name

            existing_names.append(clean_name)
            current_index += 1

        # -------------------------------------------------
        # Locate Marks table
        # -------------------------------------------------
        marks_table = None
        for t in doc.tables:
            for row in t.rows:
                if any(
                    k in clean_text(row.cells[0].text)
                    for k in [
                        "project concept",
                        "literature review",
                        "relevance",
                        "project planning",
                        "methodology",
                        "presentation"
                    ]
                ):
                    marks_table = t
                    break
            if marks_table:
                break

        if not marks_table:
            return JsonResponse(
                {"status": "error", "message": "Marks table not found"},
                status=500
            )

        # -------------------------------------------------
        # Criteria map + total row
        # -------------------------------------------------
        criteria_map = {}
        total_row = None

        for i, row in enumerate(marks_table.rows):
            t0 = clean_text(row.cells[0].text)

            if "total" in t0:
                total_row = i

            for key in [
                "project concept",
                "literature review",
                "relevance",
                "project planning",
                "methodology",
                "presentation"
            ]:
                if key in t0:
                    criteria_map[key] = i

        if total_row is None:
            return JsonResponse(
                {"status": "error", "message": "Total row not found"},
                status=500
            )

        # -------------------------------------------------
        # Member → S.No map
        # -------------------------------------------------
        member_to_sno = {}
        for r in members_table.rows[1:]:
            if len(r.cells) > 3 and r.cells[3].text.strip():
                name = r.cells[3].text.strip().lower()
                sno = r.cells[0].text.strip()
                member_to_sno[name] = sno

        print("[DEBUG] Member → S.No:", member_to_sno)

        # -------------------------------------------------
        # Insert marks
        # -------------------------------------------------
        for member_key, marks_list in evaluations.items():
            name = member_key.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(name)

            if not sno:
                continue

            col = 3 + int(sno)  # ✅ correct column mapping

            if col >= len(marks_table.rows[0].cells):
                continue

            marks_dict = {}
            for item in marks_list:
                if "-" in item:
                    crit, val = item.rsplit("-", 1)
                    try:
                        marks_dict[crit.strip()] = int(val.lstrip("0") or "0")
                    except:
                        pass

            total = 0

            for crit, mark in marks_dict.items():
                ckey = clean_text(crit)
                row_index = next(
                    (
                        criteria_map[k]
                        for k in criteria_map
                        if k in ckey or ckey in k
                    ),
                    None
                )

                if row_index is not None:
                    marks_table.rows[row_index].cells[col].text = str(mark)
                    total += mark

            marks_table.rows[total_row].cells[col].text = str(total)

        # -------------------------------------------------
        # Safe save
        # -------------------------------------------------
        try:
            doc.save(output_path)
        except PermissionError:
            ts = time.strftime("%Y%m%d_%H%M%S")
            alt_path = os.path.join(
                output_dir,
                f"{team_name_fs}_ZerothReview_{ts}.docx"
            )
            doc.save(alt_path)
            output_path = alt_path

        return JsonResponse(
            {
                "status": "success",
                "message": "Marks inserted successfully",
                "file_path": output_path
            }
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )


from django.http import FileResponse, JsonResponse # type: ignore
import os
from django.conf import settings


from django.shortcuts import redirect
from django.http import JsonResponse

def download_docx(request, team_name):
    """
    📥 Download Zeroth Review DOCX (CLOUDINARY ONLY)
    """

    if not team_name:
        return JsonResponse(
            {"status": "fail", "message": "Invalid team name"},
            status=400
        )

    # -------------------------------------------------
    # Get allocation by team name
    # -------------------------------------------------
    allocation = AllocationResult.objects.filter(
        team_name=team_name
    ).first()

    if not allocation:
        return JsonResponse(
            {"status": "fail", "message": "Team not found"},
            status=404
        )

    # -------------------------------------------------
    # Cloudinary DOCX URL
    # -------------------------------------------------
    docx_url = allocation.zeroth_review_docx_url

    if not docx_url:
        return JsonResponse(
            {
                "status": "fail",
                "message": "DOCX not uploaded to Cloudinary"
            },
            status=404
        )

    print(f"[DEBUG] Redirecting to Cloudinary DOCX: {docx_url}")

    # -------------------------------------------------
    # Redirect to Cloudinary (download handled by Cloudinary)
    # -------------------------------------------------
    return redirect(docx_url)

import os
import pdfkit
from django.http import FileResponse, JsonResponse
from django.conf import settings
from docx import Document
from tempfile import NamedTemporaryFile

def download_pdf(request, team_name):
    """
    📥 Download Zeroth Review PDF (CLOUDINARY ONLY)
    """

    if not team_name:
        return JsonResponse(
            {"status": "fail", "message": "Invalid team name"},
            status=400
        )

    # -------------------------------------------------
    # Fetch allocation
    # -------------------------------------------------
    allocation = AllocationResult.objects.filter(
        team_name=team_name
    ).first()

    if not allocation:
        return JsonResponse(
            {"status": "fail", "message": "Team not found"},
            status=404
        )

    # -------------------------------------------------
    # Cloudinary PDF URL
    # -------------------------------------------------
    pdf_url = allocation.zeroth_review_pdf_url

    if not pdf_url:
        return JsonResponse(
            {
                "status": "fail",
                "message": "PDF not uploaded to Cloudinary"
            },
            status=404
        )

    print(f"[DEBUG] Redirecting to Cloudinary PDF: {pdf_url}")

    # -------------------------------------------------
    # Redirect (Cloudinary handles download)
    # -------------------------------------------------
    return redirect(pdf_url)

import os, json, time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from docx import Document

def clean_text(text):
    return text.strip().lower()


import json
import os
import time
from django.http import JsonResponse
from django.conf import settings
from docx import Document
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save_evaluation_review1(request):
    """
    📝 Save FIRST REVIEW Evaluation Marks into DOCX
    """

    if request.method != "POST":
        return JsonResponse(
            {"status": "fail", "message": "Invalid request method"},
            status=400
        )

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # {"member_name": [marks list]}

        if not team_name or not evaluations:
            return JsonResponse(
                {"status": "fail", "message": "Missing team name or evaluations"},
                status=400
            )

        # -------------------------------------------------
        # Safe team name (filesystem)
        # -------------------------------------------------
        team_name_fs = team_name.replace(" ", "_")

        # -------------------------------------------------
        # Paths
        # -------------------------------------------------
        template_path = os.path.join(
            settings.BASE_DIR,
            "allocation",
            "static",
            "first_review_mark.docx"
        )

        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(
            output_dir,
            f"{team_name_fs}_Review1.docx"
        )

        print("[DEBUG] Review1 output:", output_path)

        # -------------------------------------------------
        # Load existing doc OR template
        # -------------------------------------------------
        if os.path.exists(output_path):
            doc = Document(output_path)
        else:
            if not os.path.exists(template_path):
                return JsonResponse(
                    {
                        "status": "error",
                        "message": f"Template not found: {template_path}"
                    },
                    status=500
                )
            doc = Document(template_path)

        # -------------------------------------------------
        # Update title
        # -------------------------------------------------
        for para in doc.paragraphs:
            if "review 1" in para.text.lower():
                para.text = f"Review 1 Evaluation - {team_name}"
                break

        # -------------------------------------------------
        # TEAM MEMBERS table (assumed first table)
        # -------------------------------------------------
        members_table = doc.tables[0]

        start_row = 2  # after headers
        existing_names = []

        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                existing_names.append(r.cells[3].text.strip())

        current_index = len(existing_names) + 1

        for member_key in evaluations.keys():
            clean_name = member_key.replace("team_member-", "").strip()

            if clean_name in existing_names:
                continue

            row_index = start_row + (current_index - 1)
            if row_index >= len(members_table.rows):
                members_table.add_row()

            members_table.rows[row_index].cells[0].text = str(current_index)
            members_table.rows[row_index].cells[3].text = clean_name

            existing_names.append(clean_name)
            current_index += 1

        # -------------------------------------------------
        # Map member → S.NO
        # -------------------------------------------------
        member_to_sno = {}
        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                name = r.cells[3].text.strip().lower()
                sno = r.cells[0].text.strip()
                member_to_sno[name] = sno

        print("[DEBUG] Member → S.NO:", member_to_sno)

        # -------------------------------------------------
        # MARKS table (assumed second table)
        # -------------------------------------------------
        marks_table = doc.tables[1]

        # -------------------------------------------------
        # Detect TOTAL row
        # -------------------------------------------------
        total_row = None
        for i, row in enumerate(marks_table.rows):
            if "total" in row.cells[0].text.lower():
                total_row = i
                break

        if total_row is None:
            total_row = len(marks_table.rows) - 1

        # -------------------------------------------------
        # Detect S.NO → column mapping
        # -------------------------------------------------
        sno_col_map = {}
        sno_row_idx = None

        for i, row in enumerate(marks_table.rows):
            for idx, cell in enumerate(row.cells):
                if cell.text.strip().isdigit():
                    sno_col_map[cell.text.strip()] = idx
                    sno_row_idx = i
            if sno_col_map:
                break

        print("[DEBUG] S.NO → Column:", sno_col_map)

        # -------------------------------------------------
        # Insert marks
        # -------------------------------------------------
        for member_key, marks_list in evaluations.items():
            clean_name = member_key.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(clean_name)

            if not sno:
                continue

            col_idx = sno_col_map.get(sno)
            if col_idx is None:
                continue

            total = 0
            row_idx = sno_row_idx + 1

            for mark in marks_list:
                if row_idx >= total_row:
                    break
                try:
                    marks_table.rows[row_idx].cells[col_idx].text = str(mark)
                    total += int(mark)
                except:
                    pass
                row_idx += 1

            marks_table.rows[total_row].cells[col_idx].text = str(total)

        # -------------------------------------------------
        # Safe save
        # -------------------------------------------------
        try:
            doc.save(output_path)
        except PermissionError:
            ts = time.strftime("%Y%m%d_%H%M%S")
            alt = os.path.join(
                output_dir,
                f"{team_name_fs}_Review1_{ts}.docx"
            )
            doc.save(alt)
            output_path = alt

        return JsonResponse(
            {
                "status": "success",
                "message": "Review 1 marks saved successfully",
                "file_path": output_path
            }
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )

def save_evaluation_review2(request):
    """
    📝 Save Second REVIEW Evaluation Marks into DOCX
    """

    if request.method != "POST":
        return JsonResponse(
            {"status": "fail", "message": "Invalid request method"},
            status=400
        )

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # {"member_name": [marks list]}

        if not team_name or not evaluations:
            return JsonResponse(
                {"status": "fail", "message": "Missing team name or evaluations"},
                status=400
            )

        # -------------------------------------------------
        # Safe team name (filesystem)
        # -------------------------------------------------
        team_name_fs = team_name.replace(" ", "_")

        # -------------------------------------------------
        # Paths
        # -------------------------------------------------
        template_path = os.path.join(
            settings.BASE_DIR,
            "allocation",
            "static",
            "second_review_mark.docx"
        )

        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(
            output_dir,
            f"{team_name_fs}_Review2.docx"
        )

        print("[DEBUG] Review2 output:", output_path)

        # -------------------------------------------------
        # Load existing doc OR template
        # -------------------------------------------------
        if os.path.exists(output_path):
            doc = Document(output_path)
        else:
            if not os.path.exists(template_path):
                return JsonResponse(
                    {
                        "status": "error",
                        "message": f"Template not found: {template_path}"
                    },
                    status=500
                )
            doc = Document(template_path)

        # -------------------------------------------------
        # Update title
        # -------------------------------------------------
        for para in doc.paragraphs:
            if "review 2" in para.text.lower():
                para.text = f"Review 2 Evaluation - {team_name}"
                break

        # -------------------------------------------------
        # TEAM MEMBERS table (assumed first table)
        # -------------------------------------------------
        members_table = doc.tables[0]

        start_row = 2  # after headers
        existing_names = []

        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                existing_names.append(r.cells[3].text.strip())

        current_index = len(existing_names) + 1

        for member_key in evaluations.keys():
            clean_name = member_key.replace("team_member-", "").strip()

            if clean_name in existing_names:
                continue

            row_index = start_row + (current_index - 1)
            if row_index >= len(members_table.rows):
                members_table.add_row()

            members_table.rows[row_index].cells[0].text = str(current_index)
            members_table.rows[row_index].cells[3].text = clean_name

            existing_names.append(clean_name)
            current_index += 1

        # -------------------------------------------------
        # Map member → S.NO
        # -------------------------------------------------
        member_to_sno = {}
        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                name = r.cells[3].text.strip().lower()
                sno = r.cells[0].text.strip()
                member_to_sno[name] = sno

        print("[DEBUG] Member → S.NO:", member_to_sno)

        # -------------------------------------------------
        # MARKS table (assumed second table)
        # -------------------------------------------------
        marks_table = doc.tables[1]

        # -------------------------------------------------
        # Detect TOTAL row
        # -------------------------------------------------
        total_row = None
        for i, row in enumerate(marks_table.rows):
            if "total" in row.cells[0].text.lower():
                total_row = i
                break

        if total_row is None:
            total_row = len(marks_table.rows) - 1

        # -------------------------------------------------
        # Detect S.NO → column mapping
        # -------------------------------------------------
        sno_col_map = {}
        sno_row_idx = None

        for i, row in enumerate(marks_table.rows):
            for idx, cell in enumerate(row.cells):
                if cell.text.strip().isdigit():
                    sno_col_map[cell.text.strip()] = idx
                    sno_row_idx = i
            if sno_col_map:
                break

        print("[DEBUG] S.NO → Column:", sno_col_map)

        # -------------------------------------------------
        # Insert marks
        # -------------------------------------------------
        for member_key, marks_list in evaluations.items():
            clean_name = member_key.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(clean_name)

            if not sno:
                continue

            col_idx = sno_col_map.get(sno)
            if col_idx is None:
                continue

            total = 0
            row_idx = sno_row_idx + 1

            for mark in marks_list:
                if row_idx >= total_row:
                    break
                try:
                    marks_table.rows[row_idx].cells[col_idx].text = str(mark)
                    total += int(mark)
                except:
                    pass
                row_idx += 1

            marks_table.rows[total_row].cells[col_idx].text = str(total)

        # -------------------------------------------------
        # Safe save
        # -------------------------------------------------
        try:
            doc.save(output_path)
        except PermissionError:
            ts = time.strftime("%Y%m%d_%H%M%S")
            alt = os.path.join(
                output_dir,
                f"{team_name_fs}_Review2_{ts}.docx"
            )
            doc.save(alt)
            output_path = alt

        return JsonResponse(
            {
                "status": "success",
                "message": "Review 2 marks saved successfully",
                "file_path": output_path
            }
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )

def save_evaluation_review3(request):
    """
    📝 Save THIRD REVIEW Evaluation Marks into DOCX
    """
    print("hello")
    if request.method != "POST":
        return JsonResponse(
            {"status": "fail", "message": "Invalid request method"},
            status=400
        )

    try:
        data = json.loads(request.body)
        team_name = data.get("team_name")
        evaluations = data.get("evaluations")  # {"member_name": [marks list]}

        if not team_name or not evaluations:
            return JsonResponse(
                {"status": "fail", "message": "Missing team name or evaluations"},
                status=400
            )

        # -------------------------------------------------
        # Safe team name (filesystem)
        # -------------------------------------------------
        team_name_fs = team_name.replace(" ", "_")

        # -------------------------------------------------
        # Paths
        # -------------------------------------------------
        template_path = os.path.join(
            settings.BASE_DIR,
            "allocation",
            "static",
            "third_review_mark.docx"
        )

        output_dir = os.path.join(settings.BASE_DIR, "generated_docs")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(
            output_dir,
            f"{team_name_fs}_Review3.docx"
        )

        print("[DEBUG] Review3 output:", output_path)

        # -------------------------------------------------
        # Load existing doc OR template
        # -------------------------------------------------
        if os.path.exists(output_path):
            doc = Document(output_path)
        else:
            if not os.path.exists(template_path):
                return JsonResponse(
                    {
                        "status": "error",
                        "message": f"Template not found: {template_path}"
                    },
                    status=500
                )
            doc = Document(template_path)

        # -------------------------------------------------
        # Update title
        # -------------------------------------------------
        for para in doc.paragraphs:
            if "review 3" in para.text.lower():
                para.text = f"Review 3 Evaluation - {team_name}"
                break

        # -------------------------------------------------
        # TEAM MEMBERS table (assumed first table)
        # -------------------------------------------------
        members_table = doc.tables[0]

        start_row = 2  # after headers
        existing_names = []

        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                existing_names.append(r.cells[3].text.strip())

        current_index = len(existing_names) + 1

        for member_key in evaluations.keys():
            clean_name = member_key.replace("team_member-", "").strip()

            if clean_name in existing_names:
                continue

            row_index = start_row + (current_index - 1)
            if row_index >= len(members_table.rows):
                members_table.add_row()

            members_table.rows[row_index].cells[0].text = str(current_index)
            members_table.rows[row_index].cells[3].text = clean_name

            existing_names.append(clean_name)
            current_index += 1

        # -------------------------------------------------
        # Map member → S.NO
        # -------------------------------------------------
        member_to_sno = {}
        for r in members_table.rows[start_row:]:
            if len(r.cells) >= 4 and r.cells[3].text.strip():
                name = r.cells[3].text.strip().lower()
                sno = r.cells[0].text.strip()
                member_to_sno[name] = sno

        print("[DEBUG] Member → S.NO:", member_to_sno)

        # -------------------------------------------------
        # MARKS table (assumed second table)
        # -------------------------------------------------
        marks_table = doc.tables[1]

        # -------------------------------------------------
        # Detect TOTAL row
        # -------------------------------------------------
        total_row = None
        for i, row in enumerate(marks_table.rows):
            if "total" in row.cells[0].text.lower():
                total_row = i
                break

        if total_row is None:
            total_row = len(marks_table.rows) - 1

        # -------------------------------------------------
        # Detect S.NO → column mapping
        # -------------------------------------------------
        sno_col_map = {}
        sno_row_idx = None

        for i, row in enumerate(marks_table.rows):
            for idx, cell in enumerate(row.cells):
                if cell.text.strip().isdigit():
                    sno_col_map[cell.text.strip()] = idx
                    sno_row_idx = i
            if sno_col_map:
                break

        print("[DEBUG] S.NO → Column:", sno_col_map)

        # -------------------------------------------------
        # Insert marks
        # -------------------------------------------------
        for member_key, marks_list in evaluations.items():
            clean_name = member_key.replace("team_member-", "").strip().lower()
            sno = member_to_sno.get(clean_name)

            if not sno:
                continue

            col_idx = sno_col_map.get(sno)
            if col_idx is None:
                continue

            total = 0
            row_idx = sno_row_idx + 1

            for mark in marks_list:
                if row_idx >= total_row:
                    break
                try:
                    marks_table.rows[row_idx].cells[col_idx].text = str(mark)
                    total += int(mark)
                except:
                    pass
                row_idx += 1

            marks_table.rows[total_row].cells[col_idx].text = str(total)

        # -------------------------------------------------
        # Safe save
        # -------------------------------------------------
        try:
            doc.save(output_path)
        except PermissionError:
            ts = time.strftime("%Y%m%d_%H%M%S")
            alt = os.path.join(
                output_dir,
                f"{team_name_fs}_Review3_{ts}.docx"
            )
            doc.save(alt)
            output_path = alt

        return JsonResponse(
            {
                "status": "success",
                "message": "Review 2 marks saved successfully",
                "file_path": output_path
            }
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )
