# allocation/models.py
from django.db import models
from django.contrib.auth.models import User

# =========================
# STUDENT & LOGIN MODELS
# =========================

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    clas = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.cgpa})"


class Stu_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.username


# =========================
# TEAM & MENTOR MODELS
# =========================

class Team(models.Model):
    project_title = models.CharField(max_length=100, unique=True)
    student_class = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    members = models.TextField()
    member_names = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title


class Mentor_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} ({self.username})"


class Coordinator_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} ({self.username})"


class Mentor(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80)
    primary_domain = models.CharField(max_length=80)
    experience = models.IntegerField()
    alternative_domains = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.username})"


# =========================
# ALLOCATION MODELS
# =========================

class Allocate_Mentor(models.Model):
    id = models.IntegerField(primary_key=True)
    team_domain = models.CharField(max_length=50)
    mentor_domain = models.CharField(max_length=50, blank=True, null=True)
    mentor_alt_domains = models.TextField(blank=True, null=True)
    mentor_experience = models.CharField(max_length=50, blank=True, null=True)
    similarity_score = models.FloatField(default=0.0)
    reason = models.CharField(max_length=100, blank=True, null=True)
    allocated_at = models.DateTimeField(auto_now_add=True)


class AllocationResult(models.Model):
    team_name = models.CharField(max_length=100)
    team_domain = models.CharField(max_length=100)
    mentor_name = models.CharField(max_length=100)
    mentor_domain = models.CharField(max_length=100)
    alt_domains = models.TextField(blank=True)
    experience = models.CharField(max_length=50)
    similarity_score = models.FloatField()
    reason = models.TextField(blank=True)
    allocated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} -> {self.mentor_name}"


# =========================
# APPROVAL / MODIFY
# =========================

class ApprovedTeam(models.Model):
    project_title = models.CharField(max_length=200)
    student_class = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    members = models.CharField(max_length=300)
    member_names = models.CharField(max_length=300)
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title


class ModifyRequest(models.Model):
    project_title = models.CharField(max_length=200)
    student_class = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    members = models.CharField(max_length=300)
    member_names = models.CharField(max_length=300)
    change_type = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Modify: {self.project_title}"


# =========================
# ZEROTH REVIEW REMARK
# =========================

class ZerothReviewRemark(models.Model):
    team_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    remark = models.TextField()
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team_name', 'mentor_name', 'heading'],
                name='unique_zeroth_review_remark'
            )
        ]


# =========================
# 🔥 NEW: CLOUDINARY DOCUMENT MODEL
# =========================

class ProjectDocument(models.Model):
    DOC_TYPE_CHOICES = [
        ("abstract", "Abstract PDF"),
        ("report", "Final Report PDF"),
        ("ppt", "Presentation PPT"),
    ]

    team_name = models.CharField(max_length=200)
    review_stage = models.CharField(
        max_length=50,
        help_text="zeroth / first / second / third"
    )
    doc_type = models.CharField(max_length=20, choices=DOC_TYPE_CHOICES)

    # ☁️ Cloudinary URL only (no local storage)
    file_url = models.URLField(max_length=500)

    uploaded_by = models.CharField(max_length=100)  # student / mentor username
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} - {self.doc_type} ({self.review_stage})"


# =========================
# ANNOUNCEMENTS
# =========================

class Announcement(models.Model):
    ANN_TYPE_CHOICES = [
        ("deadline", "Deadline"),
        ("schedule", "Schedule"),
        ("instruction", "Instruction"),
    ]

    TARGET_CHOICES = [
        ("student", "Student"),
        ("mentor", "Mentor"),
        ("both", "Both"),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    ann_type = models.CharField(max_length=20, choices=ANN_TYPE_CHOICES)
    target_role = models.CharField(max_length=20, choices=TARGET_CHOICES)

    deadline_date = models.DateField(null=True, blank=True)
    deadline_time = models.TimeField(null=True, blank=True)
    schedule_date = models.DateField(null=True, blank=True)
    schedule_time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)

    created_by_username = models.CharField(max_length=80)
    created_by_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AnnouncementStatus(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    receiver_role = models.CharField(max_length=20)
    receiver_id = models.CharField(max_length=80)
    receiver_name = models.CharField(max_length=80)
    seen_at = models.DateTimeField(null=True, blank=True)
    acknowledged_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.receiver_name} → {self.announcement.title}"
    
class ProjectFile(models.Model):
    team_name = models.CharField(max_length=200)  # just team name, no FK
    review_type = models.CharField(max_length=20)  # e.g., "zero"
    file_type = models.CharField(max_length=20)    # e.g., "ppt", "pdf", "abstract"
    cloudinary_url = models.URLField()             # Cloudinary URL
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} - {self.review_type} - {self.file_type}"