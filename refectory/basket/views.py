from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from orders.models import order
from menu.models import product
import json

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

def delete_product(request):
    if request.method == "POST" and request.is_ajax():
        data={'product_id': request.POST.get('product_id')}
        # json_dist = json.dumps(data)
        # print(json_dist)
        dist = json.loads(json.dumps(data))
        this_product = product.objects.get(id=int(dist['product_id']))

        # print(this_product)
        orders = order.objects.filter(user=request.user, status_pay=False)
        this_order = orders[0]
        this_order.basket.remove(this_product)            
            
        # print(this_order)
        if this_order.basket.all():
            pass
        else:
            this_order.delete()
            # добавить в словарь data данные
            data['empty'] = True
            



        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404