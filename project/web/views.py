from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return(render(request, 'main.html'))

def index_menu(request):
    return(render(request, 'menu.html'))

def index_shop(request):
    return(render(request, 'shop.html'))

# Create your views here.


