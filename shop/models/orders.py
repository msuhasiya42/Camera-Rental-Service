from django.db import models
from .product import Product
from .vendorCustomer import vendorCustomer
from .userCustomer import userCustomer
import datetime

class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(userCustomer,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=70,default='',blank=True)
    phone = models.CharField(max_length=12,default='',blank=True)
    rent_date = models.DateField(default=datetime.datetime.today)
    return_date = models.DateField(default=datetime.datetime.today)

    # def __str__(self):
    #     return self.product