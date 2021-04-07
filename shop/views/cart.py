from django.shortcuts import render, redirect
# to use class based views instead of direct functions
from django.views import View
# for hashing function on password
from django.contrib.auth.hashers import check_password, make_password

# import databases tables

from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from shop.models.product import Product
from shop.models.category import Category
from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from django.views import View


class Cart(View):

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'cart': products })
