"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from allocation.views import (
    login_view, student_dashboard, mentor_dashboard, create_team, add_men, logout_view,
    mentor_list, zero_ma, allocate_view, zero_men, one_men, three_men, two_men,
    zero_review, zero_base, zero_ppt, zero_form, men_ppt, hod_dashboard, coordinator_dashboard,
    team_list, save_evaluation, clean_text, zero_stu, one_stu, two_stu, three_stu,
    approve_team, modify_team, zero_ma1, download_docx, download_pdf, one_ma,
    save_evaluation_review1,serve_pdf,save_zeroth_remark,acknowledge_announcement
)

# ✅ Import for serving files from project_docs/
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="home"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),

    path('student/dashboard/', student_dashboard, name="student_dashboard"),
    path('mentor/dashboard/', mentor_dashboard, name="mentor_dashboard"),
    path('coordinator/dashboard/', coordinator_dashboard, name="coordinator_dashboard"),
    path("student/create-team/", create_team, name="create_team"),
    path("mentor/add-mentor/", add_men, name="add_men"),
    path("allocation/", allocate_view, name="run_allocation"),
    path("mentor/zero-review/", zero_men, name="zero_men"),
    path("mentor/one-review/", one_men, name="one_men"),
    path("mentor/two-review/", two_men, name="two_men"),
    path("mentor/three-review/", three_men, name="three_men"),
    path("mentor/zero-review/zero_review/", zero_review, name="zero_review"),
    path("mentor/zero-review/zero_form/", zero_form, name="zero_form"),
    path("mentor/zero-review/zero_ppt/", zero_ppt, name="zero_ppt"),
    path("mentor/zero-review/zero_base/", zero_base, name="zero_base"),
    path("mentor/zero-review/men_ppt/", men_ppt, name="men_ppt"),
    path("hod/dashboard/", hod_dashboard, name="hod_dashboard"),
    path("coordinator/mentor_list/", mentor_list, name="men_list"),
    path("coordinator/team_list/", team_list, name="team_list"),
    path("mentor/zero-review/mark-allocate/<str:team_name>", zero_ma, name="zero_ma"),
    path('save-evaluation/', save_evaluation, name='save_evaluation'),
    path('clean-text/', clean_text, name='clean_text'),
    path("student/zero-review/", zero_stu, name="zero_stu"),
    path("student/zero-review/File Upload/zeroth_remark", save_zeroth_remark, name="save_zeroth_remark"),
    path("student/one-review/", one_stu, name="one_stu"),
    path("student/two-review/", two_stu, name="two_stu"),
    path("student/three-review/", three_stu, name="three_stu"),
    path('approve_team/<str:project_title>/', approve_team, name='approve_team'),
    path('modify_team/<str:project_title>/', modify_team, name='modify_team'),
    path("student/zero-review/File Upload/", zero_ma1, name="zero_ma1"),
    path('download/<str:team_name>/docx/', download_docx, name='download_docx'),
    path('download/<str:team_name>/pdf/', download_pdf, name='download_pdf'),
    path('mentor/one-review/mark-allocate/<str:team_name>', one_ma, name='one_ma'),
    path('save-evaluation-review1/', save_evaluation_review1, name='save_evaluation_review1'),
    path('coordinator/team-list/approve/<str:project_title>/', approve_team, name='approve_team'),
    path('coordinator/team-list/modify/<str:project_title>/', modify_team, name='modify_team'),
    path('mentor/pdf/<str:team_name>/<str:pdf_type>/', serve_pdf, name='serve_pdf'),
    path("student/ack/<int:status_id>/", acknowledge_announcement, name="ack_announcement"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)