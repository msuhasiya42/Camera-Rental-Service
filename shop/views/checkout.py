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


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('username')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)


        for product in products:
            order = Order(
                product=product,
                # send email to usercustomer table and
                # assign it to customer
                customer=userCustomer(email=customer),
                price=product.price,
                address=address,
                phone=phone)


            order.placeOrder()

        request.session['cart'] = {}
        return redirect('cart')
