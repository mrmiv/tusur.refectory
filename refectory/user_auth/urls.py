from django.urls import path
from django.conf.urls import url
from user_auth import views as login_views
from general import views as general_views

urlpatterns = [
    url(r'^$', login_views.UserLogin, name='login'),
    url(r'logout$', login_views.UserLogout, name='logout'),
    url(r'^registration$', login_views.register, name='register')
]