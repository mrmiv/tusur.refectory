from django.conf.urls import url
from . import views as basket_views

urlpatterns = [
    url(r'^$', basket_views.index, name='basket_page'),
    url(r'^pay$', basket_views.pay, name='pay'),
    url(r'^delete$', basket_views.delete_product, name='delete'),
    url(r'^remove$', basket_views.remove_product, name = 'remove'),
    url(r'^add$', basket_views.add_product, name = 'add'),
]