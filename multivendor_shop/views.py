from django.shortcuts import render
from app.models import Category, Product

from django.contrib.auth import authenticate, login, logout
from app.models import UserCreateForm

def master(request):
    return render(request, 'master.html',{})


def index(request):
    category = Category.objects.all()
    
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        product = Product.objects.filter(subcategory = categoryID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category' : category,
        'product' : product,
    }

    return render(request, 'index.html', context)


def signup(request):
    print('signup called')
    return render(request, 'registration/signup.html',{})