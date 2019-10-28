
from django.contrib import admin
from django.urls import path, include
from user_auth import views as user_views
from general import views as general_views

urlpatterns = [
    # path('', include('general.urls')),
    path('', general_views.index),
    path('login/', include('user_auth.urls')),
    path('menu/', include('menu.urls')),
    path('basket/', include('basket.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
]
