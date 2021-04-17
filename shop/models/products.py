from django.db import models
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='upload/products/',null=True,blank=True)
    #cascade -> if we delete category then all products of that category will be deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def unAvail(self):
        self.save()

    @staticmethod
    def get_product_by_name(name):
        return Products.objects.filter(name=name)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Products.objects.filter(category= category_id)

        else:
            return Products.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in = ids)

    # @staticmethod
    # def get_product_by_name(name):
    #     return Product.objects.filter(name = name)

