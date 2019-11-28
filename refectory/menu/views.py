from django.shortcuts import render
from django.http import  Http404, HttpResponse
from django.shortcuts import render, redirect
from .models import product
from orders.models import order, basket
import json

def index(request):
    # products = {
    #     'Супы':product.objects.filter(category='1'),
    #     'Гарниры':product.objects.filter(category='2'),
    #     'Горячие блюда':product.objects.filter(category='3'),
    #     'Салаты':product.objects.filter(category='4'),
    #     'Завтраки':product.objects.filter(category='5'),
    #     'Выпечка':product.objects.filter(category='6'),
    #     'Дополнительно':product.objects.filter(category='7'),
    # }

    products = product.objects.all
    categories = [
        'Супы',
        'Гарниры',
        'Горячие блюда',
        'Салаты',
        'Завтраки',
        'Выпечка',
        'Другое'
    ]
    try:
        order_now = order.objects.get(user=request.user, status_pay=False)
        in_basket = basket.objects.filter(order=order_now)
        basket_items = []
        for i in in_basket:
            # print(i.product)
            basket_items.append(i.product)
        context = {'page':'Меню', 'products': products, 'categories':categories, 'basket':basket_items}
    except:
        context = {'page':'Меню', 'products': products, 'categories':categories}
    # print(products)
    return render(request, 'menu_page.html', context)

def add_product(request):
    if request.method == "POST" and request.is_ajax:
        data={
            'product_id': request.POST.get('product_id')
        }
        json_dist = json.dumps(data)
        # print(json_dist)
        dist = json.loads(json_dist)
        this_product = product.objects.get(id=int(dist['product_id']))
        
        this_order, created = order.objects.get_or_create(user=request.user, status_pay=False)


        try:
            pib = basket.objects.get(order=this_order, product=this_product)
            # print ('получили продукт',pib)
            pib.delete()
            if not this_order.products.all():
                this_order.delete()
        except basket.DoesNotExist:
            basket.objects.create(order=this_order, product=this_product)
        finally:
            pass

        # if basket.objects.filter(order=this_order, product=this_product):
        #     print('товар есть в корзине')
        #     pib = basket.objects.filter(order=this_order).get(product=this_product) #product in basket
        
        
        
        # data['error']='Что-то пошло не так :('
        # if basket.objects.filter(order=this_order, product=this_product):
        #     # print('товар есть в корзине')
        #     pib = basket.objects.filter(order=this_order).get(product=this_product) #product in basket
        #     pib.quantity += int(dist['product_quantity'])
        #     if pib.quantity >5:
        #         print('true')
        #         data['error']='В корзине не может быть больше пяти порций товара!'
        #     else:
        #         print('false')
        #         pib.save()
        # else:
        #     # print('товара нет в корзине')
        #     this_order.products.add(this_product)
        #     pib = basket.objects.filter(order=this_order).get(product=this_product) #product in basket
        #     pib.quantity = int(dist['product_quantity'])
        #     if pib.quantity >5:
        #         data['error']='В корзине не может быть больше пяти порций товара!'
        #     else:
        #         pib.save()

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404