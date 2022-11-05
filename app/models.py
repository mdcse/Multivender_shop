from dataclasses import fields
from pyexpat import model
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
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
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'product_image')
    name = models.CharField(max_length = 150)
    price = models.IntegerField()
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists':'Email all ready exists'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password')
    def save(self, commit: True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']