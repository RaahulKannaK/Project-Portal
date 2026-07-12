"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from allocation.views import (
    # ---------------- Auth & Dashboards ----------------
    login_view, student_dashboard, mentor_dashboard, coordinator_dashboard, logout_view,
    
    # ---------------- HOD Dashboard ----------------
    hod_dashboard,    # HOD ML Allocation
    hod_run_allocation, hod_save_allocations,
    
    # ---------------- HOD API Endpoints ----------------
    api_students, api_mentors, api_teams, api_allocations,
    api_unallocated_teams, api_available_students, api_reviews, api_announcements,
    
    # ---------------- HOD Actions - Students ----------------
    hod_students, hod_add_student, hod_delete_student,
    
    # ---------------- HOD Actions - Mentors ----------------
    hod_mentors, hod_add_mentor, hod_delete_mentor,
    
    # ---------------- HOD Actions - HODs (NEW) ----------------
    hod_hods, hod_add_hod, hod_delete_hod,
    
    
    # ---------------- HOD Actions - Teams ----------------
    hod_teams, hod_create_team, hod_edit_team, hod_delete_team, hod_update_team_status,
    
    # ---------------- HOD Actions - Allocations ----------------
    hod_allocations, hod_manual_allocate, hod_delete_allocation, hod_reallocate_team,
    
    # ---------------- HOD Actions - Reviews ----------------
    hod_reviews, hod_view_team_remarks,
    
    # ---------------- HOD Actions - Announcements ----------------
    hod_announcements, hod_create_announcement, hod_delete_announcement,
    
    # ---------------- HOD Actions - Reports & Settings ----------------
    hod_reports, hod_reset_password, hod_search, hod_export_csv, hod_clear_all_data,
    
    # ---------------- Team & Allocation ----------------
    create_team, add_men, allocate_view, save_allocations,
    mentor_list, team_list, approve_team, modify_team,
    
    # ---------------- Mentor Reviews ----------------
    zero_men, one_men, two_men, three_men,
    zero_review, zero_base, zero_ppt, men_ppt,
    one_ppt, two_ppt, three_ppt,
    zero_ma, one_ma, two_ma, three_ma,
    
    # ---------------- PDF.js Annotation API ----------------
    save_annotation, get_annotations, delete_annotation, update_annotation, export_annotated_pdf,
    
    # ---------------- Mentor Request Re-upload ----------------
    request_reupload, request_reupload_first, request_reupload_second, request_reupload_third,
    
    # ---------------- Student Reviews ----------------
    zero_stu, one_stu, two_stu, three_stu,
    zero_ma1, one_ma1, two_ma1, three_ma1,
    
    # ---------------- Save Remarks API ----------------
    save_zeroth_remark, save_first_remark, save_second_remark, save_third_remark,
    
    # ---------------- Save / Download ----------------
    save_evaluation, save_zeroth_evaluation,
    save_evaluation_review1, save_evaluation_review2, save_evaluation_review3,
    clean_text, download_docx, download_pdf, serve_pdf, serve_temp_html,
    
    # ---------------- CSV Upload ----------------
    upload_student_csv, upload_mentor_csv, upload_hod_csv, download_csv_template,
    
    # ---------------- Announcements & Results ----------------
    student_result_view, mentor_result_view, acknowledge_announcement,
)

# Import for serving media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ==================== ADMIN & AUTH ====================
    path('admin/', admin.site.urls),
    path('', login_view, name="home"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),

    # ==================== DASHBOARDS ====================
    path('student/dashboard/', student_dashboard, name="student_dashboard"),
    path('mentor/dashboard/', mentor_dashboard, name="mentor_dashboard"),
    path('coordinator/dashboard/', coordinator_dashboard, name="coordinator_dashboard"),
    path('hod/dashboard/', hod_dashboard, name="hod_dashboard"),

    # ==================== HOD API ENDPOINTS (AJAX) ====================
    path("hod/api/students/", api_students, name="hod_api_students"),
    path("hod/api/mentors/", api_mentors, name="hod_api_mentors"),
    path("hod/api/teams/", api_teams, name="hod_api_teams"),
    path("hod/api/allocations/", api_allocations, name="hod_api_allocations"),
    path("hod/api/unallocated-teams/", api_unallocated_teams, name="hod_api_unallocated_teams"),
    path("hod/api/available-students/", api_available_students, name="hod_api_available_students"),
    path("hod/api/reviews/", api_reviews, name="hod_api_reviews"),
    path("hod/api/announcements/", api_announcements, name="hod_api_announcements"),

    # ==================== HOD ACTIONS - STUDENTS ====================
    path("hod/students/", hod_students, name="hod_students"),
    path("hod/students/add/", hod_add_student, name="hod_add_student"),
    path("hod/students/delete/<str:student_id>/", hod_delete_student, name="hod_delete_student"),

    # ==================== HOD ACTIONS - MENTORS ====================
    path("hod/mentors/", hod_mentors, name="hod_mentors"),
    path("hod/mentors/add/", hod_add_mentor, name="hod_add_mentor"),
    path("hod/mentors/delete/<str:username>/", hod_delete_mentor, name="hod_delete_mentor"),

    # ==================== HOD ACTIONS - HODS (NEW DEDICATED TABLE) ====================
    path("hod/hods/", hod_hods, name="hod_hods"),
    path("hod/hods/add/", hod_add_hod, name="hod_add_hod"),
    path("hod/hods/delete/<str:username>/", hod_delete_hod, name="hod_delete_hod"),

    # ==================== HOD ACTIONS - TEAMS ====================
    path("hod/teams/", hod_teams, name="hod_teams"),
    path("hod/teams/create/", hod_create_team, name="hod_create_team"),
    path("hod/teams/edit/<int:team_id>/", hod_edit_team, name="hod_edit_team"),
    path("hod/teams/delete/<int:team_id>/", hod_delete_team, name="hod_delete_team"),
    path("hod/teams/status/<int:team_id>/", hod_update_team_status, name="hod_update_team_status"),

    # ==================== HOD ACTIONS - ALLOCATIONS ====================
    path("hod/allocations/", hod_allocations, name="hod_allocations"),
    path("hod/allocations/manual/", hod_manual_allocate, name="hod_manual_allocate"),
    path("hod/allocations/delete/<int:allocation_id>/", hod_delete_allocation, name="hod_delete_allocation"),
    path("hod/allocations/reallocate/", hod_reallocate_team, name="hod_reallocate_team"),

    # ==================== HOD ACTIONS - REVIEWS ====================
    path("hod/reviews/", hod_reviews, name="hod_reviews"),
    path("hod/reviews/team/<str:team_name>/", hod_view_team_remarks, name="hod_view_team_remarks"),

    # ==================== HOD ACTIONS - ANNOUNCEMENTS ====================
    path("hod/announcements/", hod_announcements, name="hod_announcements"),
    path("hod/announcements/create/", hod_create_announcement, name="hod_create_announcement"),
    path("hod/announcements/delete/<int:ann_id>/", hod_delete_announcement, name="hod_delete_announcement"),

    # ==================== HOD ACTIONS - REPORTS & SETTINGS ====================
    path("hod/reports/", hod_reports, name="hod_reports"),
    path("hod/password/reset/", hod_reset_password, name="hod_reset_password"),
    path("hod/search/", hod_search, name="hod_search"),
    path("hod/export/csv/", hod_export_csv, name="hod_export_csv"),
    path("hod/clear-all-data/", hod_clear_all_data, name="hod_clear_all_data"),

    # ==================== TEAM & ALLOCATION ====================
    path("student/create-team/", create_team, name="create_team"),
    path("mentor/add-mentor/", add_men, name="add_men"),
    # Coordinator allocation (kept for coordinator)
    path("allocation/", allocate_view, name="run_allocation"),
    
    # HOD ML Allocation (HOD style)
    path("hod/allocations/run/", hod_run_allocation, name="hod_run_allocation"),
    path("hod/allocations/save/", hod_save_allocations, name="hod_save_allocations"),
    path('save-allocations/', save_allocations, name='save_allocations'),
    path("coordinator/mentor_list/", mentor_list, name="men_list"),
    path("coordinator/team_list/", team_list, name="team_list"),
    path('approve_team/<str:project_title>/', approve_team, name='approve_team'),
    path('modify_team/<str:project_title>/', modify_team, name='modify_team'),
    path('coordinator/team-list/approve/<str:project_title>/', approve_team, name='approve_team'),
    path('coordinator/team-list/modify/<str:project_title>/', modify_team, name='modify_team'),

    # ==================== MENTOR REVIEWS ====================
    path("mentor/zero-review/", zero_men, name="zero_men"),
    path("mentor/one-review/", one_men, name="one_men"),
    path("mentor/two-review/", two_men, name="two_men"),
    path("mentor/three-review/", three_men, name="three_men"),

    # Zeroth Review sub-pages
    path("mentor/zero-review/zero_review/", zero_review, name="zero_review"),
    path("mentor/zero-review/zero_ppt/", zero_ppt, name="zero_ppt"),
    path("mentor/zero-review/zero_base/", zero_base, name="zero_base"),
    path("mentor/zero-review/men_ppt/", men_ppt, name="men_ppt"),

    # First, Second, Third Review PPT pages
    path("mentor/one-review/one_ppt/", one_ppt, name="one_ppt"),
    path("mentor/two-review/two_ppt/", two_ppt, name="two_ppt"),
    path("mentor/three-review/three_ppt/", three_ppt, name="three_ppt"),

    # Mark allocation pages
    path("mentor/zero-review/mark-allocate/<str:team_name>/", zero_ma, name="zero_ma"),
    path("mentor/one-review/mark-allocate/<str:team_name>/", one_ma, name="one_ma"),
    path("mentor/two-review/mark-allocate/<str:team_name>/", two_ma, name="two_ma"),
    path("mentor/three-review/mark-allocate/<str:team_name>/", three_ma, name="three_ma"),

    # ==================== PDF.js ANNOTATION API ====================
    path("api/save-annotation/", save_annotation, name="save_annotation"),
    path("api/get-annotations/", get_annotations, name="get_annotations"),
    path("api/delete-annotation/", delete_annotation, name="delete_annotation"),
    path("api/update-annotation/", update_annotation, name="update_annotation"),
    path("api/export-annotated-pdf/", export_annotated_pdf, name="export_annotated_pdf"),

    # ==================== MENTOR REQUEST RE-UPLOAD ====================
    path("mentor/request-reupload/", request_reupload, name="request_reupload"),
    path("mentor/request-reupload-first/", request_reupload_first, name="request_reupload_first"),
    path("mentor/request-reupload-second/", request_reupload_second, name="request_reupload_second"),
    path("mentor/request-reupload-third/", request_reupload_third, name="request_reupload_third"),

    # ==================== STUDENT REVIEWS ====================
    path("student/zero-review/", zero_stu, name="zero_stu"),
    path("student/zero-review/file-upload/", zero_ma1, name="zero_ma1"),
    path("student/one-review/", one_stu, name="one_stu"),
    path("student/one-review/file-upload/", one_ma1, name="one_ma1"),
    path("student/two-review/", two_stu, name="two_stu"),
    path("student/two-review/file-upload/", two_ma1, name="two_ma1"),
    path("student/three-review/", three_stu, name="three_stu"),
    path("student/three-review/file-upload/", three_ma1, name="three_ma1"),

    # ==================== SAVE REMARKS API ====================
    path("student/one-review/save-first-remark/", save_first_remark, name="save_first_remark"),
    path("student/two-review/save-second-remark/", save_second_remark, name="save_second_remark"),
    path("student/three-review/save-third-remark/", save_third_remark, name="save_third_remark"),
    path('save-zeroth-remark/', save_zeroth_remark, name='save_zeroth_remark'),

    # ==================== SAVE / DOWNLOAD ====================
    path('save-zeroth-evaluation/', save_zeroth_evaluation, name='save_zeroth_evaluation'),
    path('save-evaluation/', save_evaluation, name='save_evaluation'),
    path('save-evaluation-review1/', save_evaluation_review1, name='save_evaluation_review1'),
    path('save-evaluation-review2/', save_evaluation_review2, name='save_evaluation_review2'),
    path('save-evaluation-review3/', save_evaluation_review3, name='save_evaluation_review3'),
    path('clean-text/', clean_text, name='clean_text'),
    path('download/<str:team_name>/docx/', download_docx, name='download_docx'),
    path('download/<str:team_name>/pdf/', download_pdf, name='download_pdf'),
    path('mentor/pdf/<str:team_name>/<str:pdf_type>/', serve_pdf, name='serve_pdf'),
    path("mentor/temp-html/<str:team>/<str:filename>/", serve_temp_html, name="serve_temp_html"),

    # ==================== CSV UPLOAD ====================
    path('upload/student/', upload_student_csv, name='upload_student_csv'),
    path('upload/mentor/', upload_mentor_csv, name='upload_mentor_csv'),
    path('upload/hod/', upload_hod_csv, name='upload_hod_csv'),
    path('download-template/<str:template_type>/', download_csv_template, name='download_csv_template'),

    # ==================== ANNOUNCEMENTS & RESULTS ====================
    path("student/my-mentor/", student_result_view, name="student_mentor"),
    path("mentor/my-teams/", mentor_result_view, name="mentor_teams"),
    path("student/ack/<int:status_id>/", acknowledge_announcement, name="ack_announcement"),
]

# Serve media files in debug
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)