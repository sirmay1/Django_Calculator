from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "mathapp/index.html", {})

def main(request):
    return render(request, "mathapp/main.html", {})