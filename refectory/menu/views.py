from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    context = {'page':'Меню'}
    return render(request, 'menu_page.html', context)
