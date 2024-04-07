from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Blogs home page")

def about(request):
    return HttpResponse("Welcome to Blogs about page")
