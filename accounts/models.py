from django.db import models

# Create your models here.


class users(models.Model):

    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.user_id
