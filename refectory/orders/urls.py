from django.conf.urls import url
from . import views as orders_views

urlpatterns = [
    url(r'^$', orders_views.index, name='orders'),
    url(r'^get_order$', orders_views.get_order, name='get_order'),
    url(r'^refresh$', orders_views.refresh, name='refresh'),
]