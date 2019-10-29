from django.http import HttpResponse
from django.shortcuts import render, redirect, Http404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, UserCreationForm
from general import views as general_views

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            lastname = form.cleaned_data['lastname'] #фамилия
            firstname = form.cleaned_data['firstname'] #имя
            middlename = form.cleaned_data['middlename'] #отчество
            user = authenticate( 
                username = email, 
                password = password, 
                lastname = lastname,
                firstname = firstname,
                middlename = middlename,
                )
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm(request.POST)
    context = {'form': form }
    return render(request, 'register.html', context)

def UserLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user= authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # context= {'form': form,
                #       'error': 'The login has been successful'}
                return redirect('/')
            else:
                context= {'form': form,
                      'error': 'Некорректные email и/или пароль'}
            # Проверка правильности логина и пароля, и существования юзера
                return render(request, 'login.html', context)   
    else:
        context= {'form': form}
        return render(request, 'login.html', context)

def UserLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/")
    else: 
        raise Http404


