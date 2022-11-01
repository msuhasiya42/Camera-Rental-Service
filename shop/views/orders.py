from django.shortcuts import render, redirect
# to use class based views instead of direct functions
from django.views import View
from shop.middlewares.auth import auth_middleware
# import databases tables
from django.shortcuts import render
from shop.models.products import Products
from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from shop.models.orders import Order
from django.views import View
from django.utils.decorators import method_decorator


class OrderView(View):
    # it is middleware(decorator)


    def get(self, request):
        email = request.session.get('username')
        orders = Order.get_orders_by_customer(email)
        print("orders:",orders)
        for order in orders:
            product= Products.get_product_by_name(order)
            print("product:",product[0])
            p = product[0]
            if order.order_status == True:
                print(order.order_status)
                p.available = True
                p.save()
            else:
                print(order.order_status)
                p.available = False
                p.save()

        orders = orders.reverse()
        return render(request, 'orders.html',
                      {
                          'orders': orders
                      })
