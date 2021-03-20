from django.contrib import admin
#to use admin first use migrate then run server

# Register your models here.

from .models import vendorCustomer,userCustomer

class adminvendor(admin.ModelAdmin):
    #to show the details outside
    list_display = ["full_name"]

admin.site.register(vendorCustomer,adminvendor)
admin.site.register(userCustomer)




