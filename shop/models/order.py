from django.db import models
from .product import Product
from .vendorCustomer import vendorCustomer
from .userCustomer import userCustomer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(userCustomer, on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    rent_date = models.DateField(default=datetime.datetime.today)
    return_date = models.DateField(default=datetime.datetime.today)

    # status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-rentdate')
