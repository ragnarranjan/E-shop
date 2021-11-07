from django.db import models
from .category import Category


class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,default=1,null = True, blank=True)
    discription = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to = 'uploads/product_image/')


    def __str__(self):
        return self.name

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()

