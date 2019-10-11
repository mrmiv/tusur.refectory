from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django import forms
from .models import food
import json

def index(request):
    eat = food.objects.all()
    return(render(request, 'main.html',{"food": eat}))

def index_menu(request):
    return(render(request, 'menu.html'))

def index_shop(request):
    return(render(request, 'shop.html'))

# Create your views here.

# def index_menu_test(request):
#     foodform = Food_form()
#     # return render(request, "menu.html", {"form": foodform})
#     if request.method == "POST":
#         name = request.POST.get("name")
#         count = request.POST.get("count")     # получение значения поля age
#         return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#     else:
#         foodform = Food_form()
#         return render(request, "menu.html", {"form": foodform})

def test_get(request):
    eat = food.objects.all()
    return render(request, "shop.html", {"food": eat})
 
# сохранение данных в бд
def test_create(request):
    if request.method == "POST":
        tea = food()
        tea.name=request.POST.get("name")
        tea.save()
    return HttpResponseRedirect("/")

# def product(request, product_id):
#     product = food.objects.get(id=product_id)

#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#     print(request.session.session_key)
#     return render(request, "menu.html", locals())


