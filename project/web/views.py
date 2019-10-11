from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import food

def index(request):
    return(render(request, 'main.html'))

def index_menu(request):
    return(render(request, 'menu.html'))

def index_shop(request):
    return(render(request, 'shop.html'))

# Create your views here.

class Food_form(forms.Form):
    name = forms.CharField()
    count = forms.IntegerField()
    price = forms.FloatField()


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
    return render(request, "menu.html", {"food": eat})
 
# # сохранение данных в бд
# def test_create(request):
#     if request.method == "POST":
#         tea = food()
#         tea.name = request.POST.get("name")
#         tea.count = request.POST.get("count")
#         tea.price = request.POST.get("price")
#         tea.save()
#         tea = food.objects.create(name=tea.name, count=tea.count, price=tea.price)
#     return HttpResponseRedirect("menu")