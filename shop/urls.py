from django.urls import path

from . import views
from .views.logout import logout
from .views.regis import regis
from .views.login import login,logout
from .views.home import home
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from shop.middlewares.auth import auth_middleware

# Blank for home page
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('login/', login.as_view(), name='login'),
    path('regis/', regis.as_view(), name='regis'),
    path('logout/',logout, name='logout'),
    path('cart/',Cart.as_view(), name='cart'),
    path('checkout/',Checkout.as_view(), name='checkout'),
    path('orders/', auth_middleware(OrderView.as_view()) , name='Orders'),


]
