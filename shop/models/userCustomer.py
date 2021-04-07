from django.db import models

class userCustomer(models.Model):
    full_name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    email= models.EmailField(primary_key=True,max_length=50)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name

    def isExist1(self):
        if userCustomer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_customer_by_email(email):
        return userCustomer.objects.get(email=email)