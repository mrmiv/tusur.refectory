from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from orders.models import order, basket
from menu.models import product
import json

def index(request):
    if request.user.is_authenticated:
        try:
            order_now = order.objects.get(user=request.user, status_pay=False)
            
            order_now.get_total_price()

            basket_items = basket.objects.filter(order=order_now)
            # print(basket.objects.get(order=order_now))
            context = {
            'page':'Корзина', 
            'order':order_now, 
            'basket_items':basket_items
            }
            return render(request, 'shop_page.html', context)
        except:
            return render(request, 'shop_page.html', {'page':'Корзина'})
    else:
        raise Http404

def pay(request):
    order_now = order.objects.get(user=request.user, status_pay=False)    
    if order_now and request.method == "POST":
        order_now.status_pay = True
        order_now.save()
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
        this_order = order.objects.get(user=request.user, status_pay=False)
        this_order.products.remove(this_product)

        this_order.get_total_price()
        # добавить в словарь data данные
        data['total_price'] = str(this_order.total_price)            
            
        # print(this_order)
        if this_order.products.all():
            pass
        else:
            this_order.delete()
            data['empty'] = True
            
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404