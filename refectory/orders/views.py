from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import order

def index(request):
    if request.user.is_authenticated:
        orders = order.objects.all()
        for one_order in orders:
            price = 0
            for one_product in one_order.basket.all():
                price += one_product.price
            one_order.total_price = price
            one_order.save()
            print (one_order.total_price)
        context = {'page':'Заказы','orders':orders}
        return render(request, 'orders_page.html', context)
    else:
        raise Http404