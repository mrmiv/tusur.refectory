from django.shortcuts import render

def index(request):
    return(render(request, 'web/templates/main.html'))

# Create your views here.
