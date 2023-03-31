from django.shortcuts import render, redirect
from authapp.models import About
# Create your views here.

def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request, "about.html")
