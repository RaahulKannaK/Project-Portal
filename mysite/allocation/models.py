# allocation/models.py
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    clas = models.CharField(max_length=50)
    def __str__(self):
        return self.name,self.cgpa
    

class Stu_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.username    


class Team(models.Model):
    project_title = models.CharField(max_length=100, unique=True)  # user-entered title
    student_class = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    members = models.TextField()          # comma-separated roll numbers
    member_names = models.TextField()     # comma-separated student names
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title


    
class Mentor_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
# Example: CSE, IT, ECE

    def __str__(self):
        return f"{self.name} ({self.username})"
    
class Coordinator_Login(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
# Example: CSE, IT, ECE

    def __str__(self):
        return f"{self.name} ({self.username})"

class Mentor(models.Model):
    username = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=80)
    primary_domain = models.CharField(max_length=80)
    experience = models.IntegerField()
    alternative_domains = models.CharField(max_length=255, blank=True, null=True)  # store as comma-separated

    def __str__(self):
        return f"{self.name} ({self.username})"
    
class Allocate_Mentor(models.Model):
    id = models.IntegerField(primary_key=True)
    team_domain = models.CharField(max_length=50)  # snapshot
    mentor_domain = models.CharField(max_length=50, blank=True, null=True)       # snapshot
    mentor_alt_domains = models.TextField(blank=True, null=True)                 # snapshot
    mentor_experience = models.CharField(max_length=50, blank=True, null=True)   # snapshot
    similarity_score = models.FloatField(default=0.0)
    reason = models.CharField(max_length=100, blank=True, null=True)
    allocated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.team.name} ({self.team_domain}) -> {self.mentor.name if self.mentor else 'Not Assigned'}"
    
class AllocationResult(models.Model):
    team_name = models.CharField(max_length=100)
    team_domain = models.CharField(max_length=100)
    mentor_name = models.CharField(max_length=100)
    mentor_domain = models.CharField(max_length=100)
    alt_domains = models.TextField(blank=True)  # comma-separated
    experience = models.CharField(max_length=50)
    similarity_score = models.FloatField()
    reason = models.TextField(blank=True)
    allocated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} -> {self.mentor_name}"
    
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
    change_type = models.CharField(max_length=100)  # stores what they want to modify
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Modify: {self.project_title} ({self.change_type})"

class ZerothReviewRemark(models.Model):
    team_name = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)   # ✅ OK
    remark = models.TextField()                  # ❌ NOT in constraint
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team_name', 'mentor_name', 'heading'],  # ✅ ONLY THESE
                name='unique_zeroth_review_remark'
            )
        ]
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

    # ✅ SIMPLE CREATOR INFO
    created_by_username = models.CharField(max_length=80)
    created_by_name = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class AnnouncementStatus(models.Model):
    announcement = models.ForeignKey(
        Announcement, on_delete=models.CASCADE
    )

    # ✅ WHO RECEIVED
    receiver_role = models.CharField(max_length=20)   # student / mentor
    receiver_id = models.CharField(max_length=80)     # student_id OR mentor username
    receiver_name = models.CharField(max_length=80)

    # ✅ STATUS
    seen_at = models.DateTimeField(null=True, blank=True)
    acknowledged_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.receiver_name} → {self.announcement.title}"
