from django.shortcuts import render
from django.http import  Http404
from django.shortcuts import render, redirect
from .models import product

def index(request):
    context = {'page':'Меню', 'products': product.objects.all}
    return render(request, 'menu_page.html', context)

def add_product(request):
    # if request.method == "POST":
    #     some_food = product.get(id=request.get('id'))
    #     some_food.count = request.get('count')

    # else:
    #     raise Http404
    pass

def delete_product(request):
    pass