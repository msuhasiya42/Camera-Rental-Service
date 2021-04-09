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


class login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        usertype = request.POST.get('usertype')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if usertype == 'vendor':
            customer = vendorCustomer.get_customer_by_email(email)
            # checks email from the databases with form email

            print(customer)
            # to check password from the DB
            flag = check_password(password, customer.password)
            if flag:
                vendorname = customer.full_name
                email = customer.email
                # to create session we can also use other attribute
                # rather than name
                request.session["vendorname"] = email

                return redirect('home')
            else:
                errormessage = 'Invalid Email or Password'
                return render(request, 'login.html', {
                    'error': errormessage
                })
        elif usertype == 'user':
            customer = userCustomer.get_customer_by_email(email)
            print(customer)
            # checks email from the databases with form email

            flag = check_password(password,customer.password)
            if flag:
                username = customer.full_name
                email = customer.email
                request.session["username"] = email

                return redirect('home')

            else:
                errormessage = 'Invalid Email or Password'
                return render(request,'login.html',{
                    'error': errormessage
                })

        else:
            errormessage = 'Invalid Email or Password'
            return render(request, 'login.html', {
                'error': errormessage
            })

def logout(request):
    request.session.clear()
    return redirect('login')