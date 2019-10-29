from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        context = {'page':'Корзина'}
        return render(request, 'shop_page.html', context)
    else:
        raise Http404