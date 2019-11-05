
from django.contrib import admin
from django.urls import path, include
from general import views as general_views
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found, permission_denied

# handler403 = curry(permission_denied, exception=Exception('Permission Denied'), template_name='errs/403.html')
# handler404 = curry(page_not_found, exception=Exception('Page not Found'), template_name='errs/404.html')
# handler500 = curry(server_error, template_name='errs/500.html')
# handler404 = 'refectory.general.views.view_404'

urlpatterns = [
    # path('', include('general.urls')),
    path('', general_views.index),
    path('login/', include('user_auth.urls')),
    path('menu/', include('menu.urls')),
    path('basket/', include('basket.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)