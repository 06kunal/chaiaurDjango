

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("Hello, world. You are at Chai aur Django Homepage")
    return render(request, 'website/index.html')


def about(request):
    #return HttpResponse("Hello, world. You are at Chai aur Django about page")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello, world. You are at Chai aur Django contact page")
    return render(request, 'website/contact.html')

