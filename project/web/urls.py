from django.conf.urls import url
from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name="index"),
    url(r'^menu$', views.index_menu, name="menu"),
    url(r'^shop$', views.index_shop, name="shop"),
    url(r'^auth$', views.auth, name="auth"),
]