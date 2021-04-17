from django.db import models


class vendorCustomer(models.Model):
    full_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True, max_length=50)
    password = models.CharField(max_length=500)
    camera_image = models.ImageField(upload_to="upload")

    def __str__(self):
        return self.full_name

    @staticmethod
    def isExist2(email):
        if vendorCustomer.objects.filter(email=email):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        if vendorCustomer.objects.get(email=email):
          return vendorCustomer.objects.get(email=email)
        else:
            return False
