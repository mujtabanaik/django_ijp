"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web_templates.views import welcome, user_login, user_logout, signup, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('signup/', signup, name="signup"),
    path('change_password/', change_password, name="change_password"),
    path('jobs/', include('internal_jobs.urls')),
    path('employees/', include('employee.urls')),
]
