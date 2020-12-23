from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("")


def index(request):
    return render(request, 'student/student.html')

#def upload(request):
#    return render(request, 'student/upload.html')
def chat(request):
    return render(request, 'student/chat.html')
def calendar(request):
    return render(request, 'student/calendar.html')
def gradebook(request):
    return render(request, 'student/gradebook_s.html')
def submit(request):
    return render(request, 'student/submit.html')
def vassign(request):
    return render(request, 'student/vassign.html')
