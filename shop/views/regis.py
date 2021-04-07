
# to use class based views instead of direct functions
# for hashing function on password
from django.contrib.auth.hashers import check_password, make_password

# import databases tables

# Create your views here.
from django.shortcuts import render

from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from django.views import View


class regis(View):

    def get(self, request):
        return render(request, 'regis.html')

    def post(self, request):
        # to show dynamic content from the html
        usertype = request.POST.get('usertype')
        fullname = request.POST.get('fullname')
        phoneno = request.POST.get('mobileno')
        email = request.POST.get('email')
        hashpassword = make_password(request.POST.get('password'))

        # if len(fullname) < 3:
        #     errormessage = 'First name should be greater than 3 characters..!'

        # first name of variable from the models table and then variable name from the views page

        if usertype == 'vendor':
            # c1 = userCustomer()
            # c2 = vendorCustomer()
            #
            # if c1.isExist1() or c2.isExist2:
            #     errormessage = 'Email is Already Exist!'
            #     return render(request, 'regis.html', {'error': errormessage})

            photo = request.FILES['img']
            # creating the object of the customer
            customer = vendorCustomer(
                full_name=fullname,
                mobile_no=phoneno,
                email=email,
                password=hashpassword,
                camera_image=photo)

            customer.save()
            return render(request, 'login.html')
        else:
            # c1 = userCustomer()
            # c2 = vendorCustomer()
            #
            # if c1.isExist1() or c2.isExist2:
            #     errormessage = 'Email is Already Exist!'
            #     return render(request, 'regis.html', {'error': errormessage})

            customer = userCustomer(
                full_name=fullname,
                mobile_no=phoneno,
                email=email,
                password=hashpassword)
            customer.save()
            return render(request, 'login.html')



# #from django.shortcuts import render,redirect
# # to use class based views instead of direct functions
# from django.views import View
# #for hashing function on password
# from django.contrib.auth.hashers import check_password,make_password
#
# #import databases tables
#
# from django.http import HttpResponse
#
# # Create your views here.
# from django.shortcuts import render
# from .models.product import Product
# from .models.category import Category
# from .models.vendorCustomer import vendorCustomer
# from .models.userCustomer import userCustomer
#
#
# # Create your views here.