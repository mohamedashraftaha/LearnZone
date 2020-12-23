# views.py
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout, authenticate


# Create your views here.

def registerstudent(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('/UserAccount/login/student')
    else:
        form = RegisterForm

    return render(request, "user_account/register.html", {"form": form})


def registerteacher(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/UserAccount/login/teacher')
    else:
        form = RegisterForm()

    return render(request, "user_account/registerteacher.html", {"form": form})


def registerparent(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/UserAccount/login/parent')
    else:
        form = RegisterForm()

    return render(request, "user_account/registerparent.html", {"form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            request.session['password'] = password
            request.session['username'] = username

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/Student')
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="user_account/login.html",
                  context={"form": form})

def login_request_teacher(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            request.session['password'] = password
            request.session['username'] = username

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/Teacher')
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="user_account/loginteacher.html",
                  context={"form": form})

def login_request_parent(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            request.session['password'] = password
            request.session['username'] = username

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/Student')
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="user_account/loginparent.html",
                  context={"form": form})


