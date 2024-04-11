from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", { "title": "Django - Home" })

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html", { "title": "Django - About" })
