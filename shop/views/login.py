from django.shortcuts import render, redirect
# to use class based views instead of direct functions
from django.views import View
# for hashing function on password
from django.contrib.auth.hashers import check_password, make_password

# import databases tables

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from shop.models.products import Products
from shop.models.category import Category
from shop.models.vendorCustomer import vendorCustomer
from shop.models.userCustomer import userCustomer
from django.views import View


class login(View):
    # return_url = None

    def get(self, request):
        login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        login.return_url = request.GET.get('return_url')
        usertype = request.POST.get('usertype')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if usertype == 'vendor':

            # checks email from the databases with form email
            if vendorCustomer.isExist2(email):
                customer = vendorCustomer.get_customer_by_email(email)
                # to check password from the DB
                flag = check_password(password, customer.password)
                if flag:
                    vendorname = customer.full_name
                    email = customer.email
                    # to create session we can also use other attribute
                    # rather than name
                    request.session["vendorname"] = email

                    # if login.return_url:
                    #     return HttpResponseRedirect(login.return_url)
                    # else:
                        # login.return_url = None
                    return redirect('vendorpage')

            else:
                errormessage = 'Invalid Email or Password'
                return render(request, 'login.html', {
                    'error': errormessage
                })
        elif usertype == 'user':
            # checks email from the databases with form email
            if userCustomer.isExist1(email):
                customer = userCustomer.get_customer_by_email(email)
                flag = check_password(password, customer.password)
                if flag:
                    username = customer.full_name
                    email = customer.email
                    request.session["username"] = email
                    # if login.return_url:
                    #     return HttpResponseRedirect(login.return_url)
                    # else:
                        # login.return_url = None
                    return redirect('home')

                else:
                    errormessage = 'Invalid Email or Password'
                    return render(request, 'login.html', {
                        'error': errormessage
                    })

        else:
            errormessage = 'Invalid Email or Password'
            return render(request, 'login.html', {
                'error': errormessage
            })


def logout(request):
    print(request.session.get('username'))
    request.session.clear()
    return redirect('login')

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

def userprofile(request):
    if request.session.get('vendorname'):
        email = request.session.get('vendorname')
        print(email)
        customer = userCustomer.get_customer_by_email(email)
        # print("you are:", request.session.get('vendorname'))
        return render(request, 'userprofile.html',{
            'customer':customer
        })
    else:
        email = request.session.get('username')
        customer = userCustomer.get_customer_by_email(email)
        # print("You are:", request.session.get('username'))
        return render(request, 'userprofile.html', {
            'customer': customer
        })



