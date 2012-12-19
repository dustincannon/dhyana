# Create your views here.
from leaves.models import Author

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("Welcome to the leaves app. Display a random quote here.")

def authors(request):

    authors =  Author.objects.all().order_by('name')

    t = loader.get_template('authors.html')
    c = Context({
        'authors': authors,
    })

    return HttpResponse(t.render(c))

def sources(request):
    return HttpResponse("Display the list of sources here.")
