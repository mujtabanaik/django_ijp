from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.display_employee_list, name="employees"),
    path('create/', views.employee_create, name="create"),
    path('details/<int:id>/', views.employee_details, name="details"),
    path('edit/<int:id>/', views.employee_edit, name="edit"),
    path('delete/<int:id>/', views.employee_delete, name="delete"),
]
