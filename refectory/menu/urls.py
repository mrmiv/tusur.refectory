from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='menu_page'),
    url(r'^add_product$', views.add_product, name='add_product'),
]