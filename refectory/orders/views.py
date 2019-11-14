from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import order

def index(request):
    if request.user.is_authenticated:
        orders = order.objects.filter(user=request.user, status_pay=True).all()
        context = {'page':'Заказы','orders':orders}
        return render(request, 'orders_page.html', context)
    else:
        raise Http404