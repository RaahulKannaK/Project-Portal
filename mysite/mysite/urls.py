"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/ 
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from allocation.views import (
    login_view, student_dashboard, mentor_dashboard, create_team, add_men, logout_view,
    mentor_list, zero_ma, allocate_view, save_allocations, zero_men, one_men, three_men, two_men,
    zero_review, zero_base, zero_ppt, men_ppt, hod_dashboard, coordinator_dashboard,
    team_list, save_evaluation, clean_text, zero_stu, one_stu, two_stu, three_stu,
    approve_team, modify_team, zero_ma1, download_docx, download_pdf, one_ma, two_ma, three_ma,
    upload_student_csv, upload_mentor_csv, upload_hod_csv,
    save_evaluation_review1, save_evaluation_review2, save_evaluation_review3, serve_pdf,
    acknowledge_announcement, student_result_view, mentor_result_view,
    save_zeroth_evaluation,serve_temp_html,
    # 🔥 NEW: Import highlight views (legacy pipeline)
    download_csv_template,
    # ✅ NEW: First, Second, Third Review mentor PPT views
    one_ppt, two_ppt, three_ppt,
    one_ma1, two_ma1, three_ma1,
    # ✅ NEW: Save remark functions for all reviews
    save_zeroth_remark, save_first_remark, save_second_remark, save_third_remark,
    # ✅ NEW: Cloudinary upload functions
    upload_to_cloudinary, upload_to_cloudinary1, upload_to_cloudinary2, upload_to_cloudinary3,
    # ─────────────────────────────────────────────
    # ⭐ NEW: PDF.js Annotation API Views
    # ─────────────────────────────────────────────
    save_annotation,
    get_annotations,
    delete_annotation,
    update_annotation,
    export_annotated_pdf,
)

# ✅ Import for serving media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ---------------- Admin & Auth ----------------
    path('admin/', admin.site.urls),
    path('', login_view, name="home"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),

    # ---------------- Dashboards ----------------
    path('student/dashboard/', student_dashboard, name="student_dashboard"),
    path('mentor/dashboard/', mentor_dashboard, name="mentor_dashboard"),
    path('coordinator/dashboard/', coordinator_dashboard, name="coordinator_dashboard"),
    path('hod/dashboard/', hod_dashboard, name="hod_dashboard"),

    # ---------------- Team & Allocation ----------------
    path("student/create-team/", create_team, name="create_team"),
    path("mentor/add-mentor/", add_men, name="add_men"),
    path("allocation/", allocate_view, name="run_allocation"),
    path('save-allocations/', save_allocations, name='save_allocations'),
    path("coordinator/mentor_list/", mentor_list, name="men_list"),
    path("coordinator/team_list/", team_list, name="team_list"),
    path('approve_team/<str:project_title>/', approve_team, name='approve_team'),
    path('modify_team/<str:project_title>/', modify_team, name='modify_team'),
    path('coordinator/team-list/approve/<str:project_title>/', approve_team, name='approve_team'),
    path('coordinator/team-list/modify/<str:project_title>/', modify_team, name='modify_team'),

    # ---------------- Mentor Reviews ----------------
    path("mentor/zero-review/", zero_men, name="zero_men"),
    path("mentor/one-review/", one_men, name="one_men"),
    path("mentor/two-review/", two_men, name="two_men"),
    path("mentor/three-review/", three_men, name="three_men"),

    # Zeroth Review sub-pages
    # ⭐ zero_review now renders zero_review.html with PDF.js viewer
    path("mentor/zero-review/zero_review/", zero_review, name="zero_review"),
    path("mentor/zero-review/zero_ppt/", zero_ppt, name="zero_ppt"),
    path("mentor/zero-review/zero_base/", zero_base, name="zero_base"),
    path("mentor/zero-review/men_ppt/", men_ppt, name="men_ppt"),

    # ✅ NEW: First, Second, Third Review PPT pages
    path("mentor/one-review/one_ppt/", one_ppt, name="one_ppt"),
    path("mentor/two-review/two_ppt/", two_ppt, name="two_ppt"),
    path("mentor/three-review/three_ppt/", three_ppt, name="three_ppt"),

    # Mark allocation pages
    path("mentor/zero-review/mark-allocate/<str:team_name>/", zero_ma, name="zero_ma"),
    path("mentor/one-review/mark-allocate/<str:team_name>/", one_ma, name="one_ma"),
    path("mentor/two-review/mark-allocate/<str:team_name>/", two_ma, name="two_ma"),
    path("mentor/three-review/mark-allocate/<str:team_name>/", three_ma, name="three_ma"),

    # ─────────────────────────────────────────────
    # ⭐ NEW: PDF.js Annotation API Endpoints
    # ─────────────────────────────────────────────
    path("api/save-annotation/", save_annotation, name="save_annotation"),
    path("api/get-annotations/", get_annotations, name="get_annotations"),
    path("api/delete-annotation/", delete_annotation, name="delete_annotation"),
    path("api/update-annotation/", update_annotation, name="update_annotation"),
    path("api/export-annotated-pdf/", export_annotated_pdf, name="export_annotated_pdf"),


    # ---------------- Student Reviews ----------------
    path("student/zero-review/", zero_stu, name="zero_stu"),
    path("student/zero-review/file-upload/", zero_ma1, name="zero_ma1"),
    path("student/one-review/", one_stu, name="one_stu"),
    path("student/one-review/file-upload/", one_ma1, name="one_ma1"),
    path("student/two-review/", two_stu, name="two_stu"),
    path("student/two-review/file-upload/", two_ma1, name="two_ma1"),
    path("student/three-review/", three_stu, name="three_stu"),
    path("student/three-review/file-upload/", three_ma1, name="three_ma1"),

    # ---------------- Save Remarks API ----------------
    path("student/one-review/save-first-remark/", save_first_remark, name="save_first_remark"),
    path("student/two-review/save-second-remark/", save_second_remark, name="save_second_remark"),
    path("student/three-review/save-third-remark/", save_third_remark, name="save_third_remark"),

    # ---------------- Save / Download ----------------
    path('save-zeroth-remark/', save_zeroth_remark, name='save_zeroth_remark'),
    path('save-zeroth-evaluation/', save_zeroth_evaluation, name='save_zeroth_evaluation'),
    path('save-evaluation/', save_evaluation, name='save_evaluation'),
    path('save-evaluation-review1/', save_evaluation_review1, name='save_evaluation_review1'),
    path('save-evaluation-review2/', save_evaluation_review2, name='save_evaluation_review2'),
    path('save-evaluation-review3/', save_evaluation_review3, name='save_evaluation_review3'),
    path('clean-text/', clean_text, name='clean_text'),
    path('download/<str:team_name>/docx/', download_docx, name='download_docx'),
    path('download/<str:team_name>/pdf/', download_pdf, name='download_pdf'),
    path('mentor/pdf/<str:team_name>/<str:pdf_type>/', serve_pdf, name='serve_pdf'),

    # ---------------- CSV Upload ----------------
    path('upload/student/', upload_student_csv, name='upload_student_csv'),
    path('upload/mentor/', upload_mentor_csv, name='upload_mentor_csv'),
    path('upload/hod/', upload_hod_csv, name='upload_hod_csv'),
    path('download-template/<str:template_type>/', download_csv_template, name='download_csv_template'),

    # ---------------- Announcements ----------------
    path("student/my-mentor/", student_result_view, name="student_mentor"),
    path("mentor/my-teams/", mentor_result_view, name="mentor_teams"),
    path("student/ack/<int:status_id>/", acknowledge_announcement, name="ack_announcement"),
    path("mentor/temp-html/<str:team>/<str:filename>/", serve_temp_html, name="serve_temp_html"),
]

# Serve media files in debug
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)