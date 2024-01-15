from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")


def sina(request):
    return HttpResponse("hello sina.")

def zh(request):
    return HttpResponse("salam, Zahra")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})

