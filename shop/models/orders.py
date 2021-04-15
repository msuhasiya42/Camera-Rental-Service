from django.db import models
from .products import Products
from .vendorCustomer import vendorCustomer
from .userCustomer import userCustomer
import datetime


class Order(models.Model):
    first_name = models.CharField(max_length=20, default="", null=True)
    last_name = models.CharField(max_length=20, default="", null=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    customer = models.ForeignKey(userCustomer, on_delete=models.CASCADE)

    address = models.CharField(max_length=100, default="", null=True)
    city = models.CharField(max_length=50, default='',null=True)
    pincode = models.IntegerField(null=True)
    state = models.CharField(max_length=20, default='',null=True)


    rent_date = models.DateField(default=datetime.datetime.today)
    return_date = models.DateField(default=datetime.datetime.today)


    # by default
    order_status = models.BooleanField(default=False)
    # status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('rent_date')

