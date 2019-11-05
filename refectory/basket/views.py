from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from orders.models import order

def index(request):
    if request.user.is_authenticated:
        basket = order.objects.filter(user=request.user, status_pay=False)
        context = {'page':'Корзина', 'basket':basket}
        return render(request, 'shop_page.html', context)
    else:
        raise Http404

def pay(request):
    orders = order.objects.filter(user=request.user, status_pay=False)    
    if orders and request.method == "POST":
        orders[0].status_pay = True
        orders[0].save()
        # print(orders[0].id)
        return redirect('/orders')
    else:
        raise Http404