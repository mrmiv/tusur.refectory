from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return(render(request, 'main.html'))

def index_menu(request):
    return(render(request, 'menu.html'))

# Create your views here.
