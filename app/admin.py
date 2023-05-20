from django.contrib import admin

# Register your models here.
from . models import Category, SubCategory, Product, ContactUs, Order

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(Order)