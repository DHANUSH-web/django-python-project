from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!!, Welcome to Polls app")

def about(request):
    return HttpResponse("We are Polls, folks!!")
