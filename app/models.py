from ast import Delete
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length = 150)
    # foreignkey
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subcotegory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'product_image')
    name = models.CharField(max_length = 150)
    price = models.IntegerField()
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name
