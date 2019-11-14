from django.shortcuts import render
from django.http import  Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import product
from orders.models import order
import json

def index(request):
    products = {
        'Супы':product.objects.filter(category='1'),
        'Гарниры':product.objects.filter(category='2'),
        'Горячие блюда':product.objects.filter(category='3'),
        'Салаты':product.objects.filter(category='4'),
        'Завтраки':product.objects.filter(category='5'),
        'Выпечка':product.objects.filter(category='6'),
        'Дополнительно':product.objects.filter(category='7'),
    }
    # print(products)
    context = {'page':'Меню', 'products': products}
    return render(request, 'menu_page.html', context)

def category(request):
    if request.is_ajax:
        data = {'category': request.GET.get('category')}
        json_dist = json.dumps(data)
        dist = json.loads(json_dist)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

def add_product(request):
    if request.method == "POST" and request.is_ajax:
        data={'product_id': request.POST.get('product_id')}
        json_dist = json.dumps(data)
        # print(json_dist)
        dist = json.loads(json_dist)
        this_product = product.objects.get(id=int(dist['product_id']))

        # print(this_product)
        # orders = order.objects.filter(user=request.user, status_pay=False)
        
        # if not orders:
        #     this_order = order.objects.create(user=request.user)
        # else:
        #     this_order = orders[0]
        this_order, created = order.objects.get_or_create(user=request.user, status_pay=False)

        this_order.basket.add(this_product)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404