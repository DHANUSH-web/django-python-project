from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="index.html", context={ "title": "Django - Home" })

def about(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="about.html", context={ "title": "Django - About" })
