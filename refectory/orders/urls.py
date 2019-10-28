from django.conf.urls import url
from . import views as orders_views

urlpatterns = [
    url(r'^$', orders_views.index, name='login')
]