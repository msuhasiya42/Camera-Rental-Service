from django.shortcuts import render, redirect
# to use class based views instead of direct functions
from django.views import View
from shop.middlewares.auth import auth_middleware
# import databases tables
from django.shortcuts import render
from shop.models.product import Product
from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from shop.models.order import Order
from django.views import View
from django.utils.decorators import method_decorator


class OrderView(View):
    # it is middleware(decorator)

    def get(self, request):
        email = request.session.get('username')
        orders = Order.get_orders_by_customer(email)
        # orders = orders.reverse()
        return render(request, 'orders.html',
                      {
                          'orders': orders
                      })
