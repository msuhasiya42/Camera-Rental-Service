from django.shortcuts import render, redirect
# to use class based views instead of direct functions
from django.views import View

# import databases tables
from django.shortcuts import render
from shop.models.product import Product
from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from shop.models.order import Order
from django.views import View


class OrderView(View):
    def get(self,request):
        email= request.session.get('username')
        orders = Order.get_orders_by_customer(email)

        return render(request, 'orders.html',{
            'orders':orders
        })
