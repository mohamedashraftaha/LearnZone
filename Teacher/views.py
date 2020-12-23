from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("")


def index(request):
    return render(request, 'Teacher/teacher2.html')
def upload(request):
    return render(request, 'Teacher/upload.html')
def chat(request):
    return render(request, 'Teacher/chat.html')
def calendar(request):
    return render(request, 'Teacher/calendar.html')
def gradebook(request):
    return render(request, 'Teacher/gradebook_t.html')
