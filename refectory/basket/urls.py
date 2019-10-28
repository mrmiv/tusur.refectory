from django.conf.urls import url
from . import views as basket_views

urlpatterns = [
    url(r'^$', basket_views.index, name='basket_page')
]