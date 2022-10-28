from ast import Delete
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150)

class SubCategory(models.Model):
    name = models.CharField(max_length = 150)
    # foreignkey
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
