from django.conf.urls import url
from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name="index"),
    # url(r'^menu$', views.test_get, name="menu"),
    # url(r'^shop$', views.test_create, name="shop")
]