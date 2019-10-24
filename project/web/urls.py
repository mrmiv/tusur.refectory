from django.conf.urls import url
from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name="index"),
    url(r'^menu$', views.index_menu, name="menu"),
    url(r'^shop$', views.index_shop, name="shop"),
<<<<<<< HEAD
    url(r'^auth$', views.auth, name="auth") 
=======
    url(r'^auth$', views.auth, name="auth"),
>>>>>>> e5d514e5a98abf5fd7cdd1ca9aadcb0e68aee7a1
]