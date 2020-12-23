from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Homepage/hp.html')
def faqs(request):
    return render(request, 'Homepage/faq.html')
def support(request):
    return render(request, 'Homepage/support.html')
def aboutus(request):
    return render(request, 'Homepage/about.html')



