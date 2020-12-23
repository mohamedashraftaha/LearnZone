from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('FAQs', views.faqs, name='faqs'),
    path('Support', views.support, name='support'),
    path('AboutUs', views.aboutus, name='aboutus'),

]