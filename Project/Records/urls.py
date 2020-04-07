"""StudentDetails URL Configuration

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
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('Print/',views.Print,name='Student-print'),
	path('Create/',views.Create,name='Student-create'),
    path('Create/Create_student/',views.Create_student,name='New_Student_entry'),
    path('Create/Create_school/',views.Create_school,name='New_School_entry'), 
    path('Create/Create_subject/',views.Create_subject,name='New_Subject_entry'), 
    path('Create/Create_school/Create_New_school/',views.Create_New_school,name='Create_New_school'),
    path('Create/Create_student/Create_New_student/',views.Create_New_student,name='Create_New_student'), 
    path('Create/Create_subject/Create_New_subject/',views.Create_New_subject,name='Create_New_subject'),
    path('register/',views.Register,name='register'),
    path('profile/',views.Profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='Records/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Records/logout.html'),name='logout') 
] 
urlpatterns+=staticfiles_urlpatterns()