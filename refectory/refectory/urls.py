
from django.contrib import admin
from django.urls import path, include
from general import views as general_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('general.urls')),
    path('', general_views.index),
    path('login/', include('user_auth.urls')),
    path('menu/', include('menu.urls')),
    path('basket/', include('basket.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)