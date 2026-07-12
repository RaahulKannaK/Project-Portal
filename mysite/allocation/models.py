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
    project_title = models.CharField(max_length=100, unique=True, blank=True, null=True)
    student_class = models.CharField(max_length=50)
    domain = models.CharField(max_length=100, blank=True, null=True)
    members = models.TextField()
    member_names = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Leader tracking - stores the student_id of team creator
    leader_id = models.CharField(max_length=50, blank=True, null=True)
    
    # Status tracking
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('pending_update', 'Pending Update'),
        ('approved', 'Approved'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Modification tracking fields (coordinator ticks these)
    needs_update_problem = models.BooleanField(default=False)
    needs_update_domain = models.BooleanField(default=False)
    needs_update_members = models.BooleanField(default=False)
    
    # Coordinator feedback reason
    modification_reason = models.TextField(blank=True, null=True)
    
    # 🔥 NEW: Allow mentor to request re-upload from student
    reupload_allowed = models.BooleanField(default=False)
    reupload_reason = models.TextField(blank=True, null=True)
    reupload_requested_at = models.DateTimeField(null=True, blank=True)
    reupload_requested_by = models.CharField(max_length=80, blank=True, null=True)
    
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
    color = models.CharField(max_length=20, default="#ffe066")
    file_type = models.CharField(max_length=20, default="abstract")
    
    # 🔥 Use TextField to store JSON string (more compatible)
    coordinates = models.TextField(default="{}", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['team_name', 'mentor_name', 'heading']

    def __str__(self):
        return f"{self.team_name} - {self.heading[:50]}"


class FirstReviewRemark(models.Model):
    team_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    remark = models.TextField()
    color = models.CharField(max_length=20)

    # ✅ New column to identify file type (ppt for review 1)
    file_type = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.team_name} - {self.heading} ({self.file_type})"


class SecondReviewRemark(models.Model):
    team_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    remark = models.TextField()
    color = models.CharField(max_length=20)

    # ✅ New column to identify file type (ppt for review 2)
    file_type = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.team_name} - {self.heading} ({self.file_type})"


class ThirdReviewRemark(models.Model):
    team_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    remark = models.TextField()
    color = models.CharField(max_length=20)

    # ✅ New column to identify file type (ppt for review 3)
    file_type = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.team_name} - {self.heading} ({self.file_type})"

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
    
class ProjectRemarks(models.Model):
    team_name = models.CharField(max_length=200)
    review_type = models.CharField(max_length=20)      # "zero", "mid", "final"
    file_type = models.CharField(max_length=20)        # "abstract", "ppt", "report"
    mentor_name = models.CharField(max_length=100)     # who annotated
    cloudinary_url = models.URLField()                  # annotated PDF URL
    original_file = models.ForeignKey(                 # link to source file
        ProjectFile, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.team_name} - {self.review_type} - {self.mentor_name}"


from django.db import models

class Annotation(models.Model):
    HIGHLIGHT = 'highlight'
    COMMENT = 'comment'
    ANNOTATION_TYPES = [
        (HIGHLIGHT, 'Highlight'),
        (COMMENT, 'Comment'),
    ]

    team = models.ForeignKey('ProjectFile', on_delete=models.CASCADE, related_name='annotations')
    page_number = models.IntegerField()
    annotation_type = models.CharField(max_length=20, choices=ANNOTATION_TYPES, default=HIGHLIGHT)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    color = models.CharField(max_length=20, default='#FFFF00')
    selected_text = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    mentor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page_number', 'created_at']

    def __str__(self):
        return f"{self.annotation_type} on page {self.page_number} by {self.mentor}"