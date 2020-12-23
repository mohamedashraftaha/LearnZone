from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('chat', views.chat, name='chat'),
    path('calendar', views.calendar, name='calendar'),
    path('gradebook', views.gradebook, name='gradebook'),
]
