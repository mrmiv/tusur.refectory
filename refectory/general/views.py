from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    context = {'page':'main'}
    return render(request, 'main_page.html', context)
