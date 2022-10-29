from django.shortcuts import render
from app.models import Category, Product


def master(request):
    return render(request, 'master.html',{})


def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category' : category,
        'product' : product,
    }

    return render(request, 'index.html', context)