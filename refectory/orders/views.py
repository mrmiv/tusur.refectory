from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import order, basket
import json

def index(request):
    if request.user.is_authenticated and not request.user.is_staff:
        orders_get = order.objects.filter(user=request.user,status_get=False, status_pay=True).all()
        orders_gotten = order.objects.filter(user=request.user, status_get=True, status_pay=True).all()

        basket_items = basket.objects.filter(order__user=request.user)
        # print(basket_items)
        context = {
        'page':'Заказы',
        'orders_get':orders_get,
        'orders_gotten':orders_gotten,
        'basket':basket_items}
        return render(request, 'orders_page.html', context)
    elif request.user.is_authenticated and request.user.is_staff:
        orders_get = order.objects.filter(status_get=False,status_pay=True).all()
        orders_gotten = order.objects.filter(status_get=True, status_pay=True).all()

        basket_items = basket.objects.all()

        context = {
        'page':'Заказы',
        'orders_get':orders_get,
        'orders_gotten':orders_gotten,
        'basket':basket_items}
        return render(request, 'orders_page.html', context)
    else:
        raise Http404

def get_order(request):
    if request.method=="POST" and request.is_ajax():
        data={'order_to_get': request.POST.get('order_to_get')}
        # json_dist = json.dumps(data)
        # print(json_dist)
        dist = json.loads(json.dumps(data))
        # print(dist['order_to_get'])
        
        this_order = order.objects.get(
            id=int(dist['order_to_get'])
            )
        # print(this_order)
        this_order.status_get=True
        this_order.save()
            
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

def refresh(request):
    if request.method=="POST" and request.is_ajax():
        data={'refresh_order': request.POST.get('refresh_order')}
        dist = json.loads(json.dumps(data))
        # корзина товаров заказа, ктр нужно повторить
        order_to_refresh = basket.objects.filter(
            order=(dist['refresh_order'])
            )
        # print(order_to_refresh)
        # текущий заказ
        order_now, created = order.objects.get_or_create(user=request.user, status_pay=False, status_get=False)

        for every in order_to_refresh:
            # print(every.product)
            try:
                some_product = basket.objects.get(product=every.product, order=order_now)
                # print('продукт',every.product,'уже есть в корзине заказа',order_now.id,'в количестве',every.quantity)
                some_product.quantity += every.quantity
                some_product.save()
            except:
                # order_now.products.add(every)
                # print('продукта',every.product,'нет в корзине заказа',order_now.id)
                order_now.products.add(every.product)
                some_product = basket.objects.get(product=every.product, order=order_now)
                some_product.quantity = every.quantity
                some_product.save()
                # print(order_now.products.all())

        order_now.get_total_price()
        order_now.save()

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
