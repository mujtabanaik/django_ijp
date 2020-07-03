from django.urls import path, include
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.requirement_list, name="jobs"),
    path('create/', views.requirement_create, name="add"),
    path('details/<int:id>/', views.requirement_details, name="details"),
    path('edit/<int:id>/', views.requirement_edit, name="edit"),
    path('delete/<int:id>/', views.requirement_delete, name="delete"),
    path('reports/', views.job_reports, name="reports"),
    path('applicants/', views.display_job_applications, name="job_applications"),
    path('applicants/create', views.create_applicant, name="applicant_create"),
    path('applicants/edit/<int:id>/', views.edit_applicant, name="applicant_edit"),
    path('applicants/delete/<int:id>/', views.delete_applicant, name="applicant_delete"),
    path('applicants/apply/<str:request_id>', views.apply_to_job, name="apply_job"),

]
