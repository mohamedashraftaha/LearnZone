from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/student',views.registerstudent,name ='register'),
    path('login/student', views.login_request, name='login'),
    path('register/teacher', views.registerteacher, name='register'),
    path('login/teacher', views.login_request_teacher, name='login'),
    path('register/parent', views.registerparent, name='register'),
    path('login/parent',views.login_request_parent, name='login'),
    path('logout/student', auth_views.LogoutView.as_view(template_name='user_account/logout.html'), name='logout'),
    path('logout/teacher', auth_views.LogoutView.as_view(template_name='user_account/logoutteacher.html'), name='logoutt'),
    path('logout/parent', auth_views.LogoutView.as_view(template_name='user_account/logoutparent.html'), name='logoutp'),
]