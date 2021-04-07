from django.contrib import admin

# Register your models here.
from django.contrib import admin

#importing model from the folder model
from .models.product import Product
from .models.category import Category
from .models.vendorCustomer import vendorCustomer
from .models.userCustomer import userCustomer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = [
        'name','price','category'
    ]

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(vendorCustomer)
admin.site.register(userCustomer)
admin.site.register(Order)
