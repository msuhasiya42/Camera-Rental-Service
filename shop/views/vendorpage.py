

# import databases tables

# Create your views here.
from django.shortcuts import render

from shop.models.vendorCustomer import vendorCustomer

from shop.models.products import Products
from shop.models.category import Category
from django.views import View



class vendorpage(View):

    def get(self, request):
        return render(request, 'vendorpage.html')

    def post(self, request):
        # to show dynamic content from the html
        productName = request.POST.get('productname')
        img = request.POST.get('photo', False)
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')

        # getting email of logged in vendor
        customer = request.session.get('username')

        # name of camera owner and address
        fullname = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')

        newProduct = Products(
            name = productName,
            image = img,
            price = price,
            description = description,
            category = Category(name=category),
            # owner and vendor details
            vendor_email = vendorCustomer(email=customer),
            owner=fullname,
            address = address,
            phone = phone,
            pincode = pincode,
            city = city,
            state = state,)

        newProduct.addProduct()

        return render(request, 'index.html')

