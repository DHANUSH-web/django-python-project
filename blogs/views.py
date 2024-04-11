from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", dict(page="home"))

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", dict(page="about"))
