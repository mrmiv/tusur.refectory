from django.conf.urls import url
from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create_user"),

    url(r'^ajax/add$', views.ajax_post, name="ajax_post"),
    url(r'^ajax/get$', views.ajax_get, name="ajax_get"),

    url(r'^menu$', views.index_menu, name="menu"),
    url(r'^shop$', views.author_index, name="shop"),


    # url(r'ajax/add/'), views.ajax_addproduct, name="add_product")
]