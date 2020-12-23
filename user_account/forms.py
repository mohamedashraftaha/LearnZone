from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import models


class RegisterForm(UserCreationForm):  # inherit from UserCreationForm
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


