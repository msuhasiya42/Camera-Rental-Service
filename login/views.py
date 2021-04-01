from django.shortcuts import render

#for hashing function on password
from django.contrib.auth.hashers import check_password,make_password

#import databases tables
from .models import vendorCustomer,userCustomer
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.method=='POST':
        # to show dynamic content from the html
        usertype = request.POST.get('usertype')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(usertype,email,password)

        if usertype == 'vendor':

            #checks email from the databases with form email
            valid = vendorCustomer.objects.get(pk=email)
            print(valid)
            #to check password from the DB
            flag = check_password(password,valid.password)
            if flag:
                 vendorname = valid.full_name
                 #to create session
                 request.session["vendorname"]= vendorname
                 return render(request,'Home.html',{"user":vendorname})

            else:
                 return HttpResponse("invalid user...")
        else:
            # checks email from the databases with form email
            valid = userCustomer.objects.get(pk=email)
            flag = check_password(password, valid.password)
            if flag:
                username = valid.full_name
                request.session["username"] = username
                return render(request, 'Home.html', {"user": username})
            else:
                return HttpResponse("invalid user...")


    else:
        return render(request,'login.html')

def regis(request):
    if request.method == 'POST':
        # to show dynamic content from the html
        usertype = request.POST.get('usertype')
        fullname=request.POST.get('fullname')
        phoneno=request.POST.get('mobileno')
        email = request.POST.get('email')
        hashpassword = make_password(request.POST.get('password'))


        #first name of variable from the models table and then variable name from the views page

        if usertype=='vendor':
            photo = request.FILES['img']
            customer =vendorCustomer(full_name=fullname,mobile_no=phoneno, email=email, password=hashpassword, camera_image=photo)
            customer.save()
            return render(request, 'login.html')
        else:
            customer = userCustomer(full_name=fullname, mobile_no=phoneno, email=email, password=hashpassword)
            customer.save()
            return render(request, 'login.html')

    else:
        return render(request, 'regis.html')

def home(request):
    return render(request,'Home.html')
