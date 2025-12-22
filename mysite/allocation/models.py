# allocation/models.py
from django.db import models

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
