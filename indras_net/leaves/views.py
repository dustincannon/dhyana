# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the leaves app. Display a random quote here.")

def authors(request):
    return HttpResponse("Display the list of authors here.")

def sources(request):
    return HttpResponse("Display the list of sources here.")
