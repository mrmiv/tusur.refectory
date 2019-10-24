from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django import forms
# from .models import Userform, user
from django.contrib.auth import authenticate, user
import json

def index(request):
<<<<<<< HEAD
    userform = Userform()
    return(render(request, 'main.html', {"form": Userform}))
=======
    return(render(request, 'main.html',))
>>>>>>> e5d514e5a98abf5fd7cdd1ca9aadcb0e68aee7a1

def index_menu(request):
    return(render(request, 'menu.html'))

def index_shop(request):
    return(render(request, 'shop.html')) 

# def auth(request):
    # if request.method == 'POST':
    #     user_form = Userform(request.POST, instance=request.user)
    #     if user.is_anonymous():
    #         if user_form.is_valid():
    #             user_form.save()
    #             user.authenticate(name=)
    #             return HttpResponse("<h2>Hello, {0}</h2>".format(name, email))
    #         else:
    #             return 

def auth(request):
    if request.method == 'POST':
        user_form = Userform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
            # messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = Userform(instance=request.user)
        # profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main.html', {
        'user_form': user_form,
        # 'profile_form': profile_form
    })


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


