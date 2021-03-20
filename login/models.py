from django.db import models

# Create your models here.
#django creates the databases for the models created here
#always migrate database after making changes
class vendorCustomer(models.Model):
    full_name=models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10,unique=True)
    email= models.EmailField(max_length=50,unique=True)
    password= models.CharField(max_length=500)
    camera_image = models.ImageField(upload_to="upload")

    def __str__(self):
        return self.email

class userCustomer(models.Model):
    full_name=models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    email= models.EmailField(max_length=50)
    password= models.CharField(max_length=500)

    def __str__(self):
        return self.email

