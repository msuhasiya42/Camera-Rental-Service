from django.urls import path

from . import views
from .views.logout import logout
from .views.regis import regis
from .views.login import login,logout
from .views.home import home
from .views.cart import Cart

# Blank for home page
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('login/', login.as_view(), name='login'),
    path('regis/', regis.as_view(), name='regis'),
    path('logout/',login.as_view(), name='logout'),
    path('cart/',Cart.as_view(), name='cart'),

]
