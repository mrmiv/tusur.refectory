from django.shortcuts import render
from django.http import  Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import product
from orders.models import order
import json

def index(request):
    context = {'page':'Меню', 'products': product.objects.all}
    return render(request, 'menu_page.html', context)

def add_product(request):
    if request.method == "POST" and request.is_ajax:
        data={'product_id': request.POST.get('product_id')}
        json_dist = json.dumps(data)
        # print(json_dist)
        dist = json.loads(json_dist)
        this_product = product.objects.get(id=int(dist['product_id']))

        # print(this_product)
        orders = order.objects.filter(user=request.user, status_pay=False)
        
        # if not orders:
        #     this_order = order.objects.create(user=request.user)
        # else:
        #     this_order = orders[0]
        this_order, created = order.objects.get_or_create(user=request.user, status_pay=False)

        this_order.basket.add(this_product)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404