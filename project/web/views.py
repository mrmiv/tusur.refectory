from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, JsonResponse
from django import forms
from .forms import user_form
from .models import user
import json

def index(request):
    users = user.objects.all()
    return(render(request, 'main.html', {"users":users}))

def index_menu(request):
    return(render(request, 'menu.html'))

def index_shop(request):
    return(render(request, 'shop.html'))

def create(request):
    if request.method == "POST":
        someuser=user()
        someuser.name = request.POST.get("name")
        someuser.email = request.POST.get("email")
        someuser.save()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseNotFound("404 404 404")

def ajax_post(request):
    if request.is_ajax() and request.POST:
        data={'name': request.POST.get('name'), 'email':  request.POST.get('email')}

        json_dist = json.dumps(data)
        dist = json.loads(json_dist)
        
        someuser=user()
        someuser.name = dist['name']
        someuser.email = dist['email']
        someuser.save()
        
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

def ajax_get(request):
    if request.is_ajax():
        users = user.objects.all()
        data = json.dumps(users)
        print(data)
        return JsonResponse(data, content_type='application/json')
    else:
        raise Http404

def author_index(request):
    if request.method == "POST":
        userform = user()
        name = request.POST.get("name")
        email = request.POST.get("email")
        # print(users)
        if user.objects.filter(name=name, email=email):
            return HttpResponse("<h2>Hello, {0}, ur email is {1}</h2>".format(name, email))
        else:
            return HttpResponse("Такого пользователя нет")
        # return HttpResponse("Invalid data")
    else:
        userform = user()
        return render(request, "shop.html", {"form": userform})



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

# def test_get(request):
#     eat = food.objects.all()
#     return render(request, "shop.html", {"food": eat})
 
# # сохранение данных в бд
# def test_create(request):
#     if request.method == "POST":
#         tea = shop()
#         tea.name=request.POST.get("name")
#         tea.price=request.POST.get("price")
#         tea.count=request.POST.get("count")
#         tea.save()
#         # return HttpResponseRedirect("shop")
#         eat = food.objects.all()
#         return render(request, "main.html", {"food": eat})
#     else:
#         buy = shop.objects.all()
#         return render(request, "shop.html", {"shop": buy})


# def product(request, product_id):
#     product = food.objects.get(id=product_id)

#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#     print(request.session.session_key)
#     return render(request, "menu.html", locals())


