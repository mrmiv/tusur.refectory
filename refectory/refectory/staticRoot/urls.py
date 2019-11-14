from django.conf.urls import url
from . import views as general_views

urlpatterns = [
    url(r'^$', general_views.index, name='main_page')
]