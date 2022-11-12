from django.shortcuts import render, redirect
from app.models import Category, Product

from django.contrib.auth import authenticate, login, logout
from app.models import UserCreateForm

def master(request):
    return redirect('index/')


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
    if(request.method == 'POST'):
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=True)
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user),
            print('signup success')
            return redirect('/')
    else:
        form = UserCreateForm()
    # base = "http://127.0.0.1:8000"
    context = {
        'form' : form,
        # 'base' : base
    }

    return render(request, 'registration/signup.html', context)

def signin(request):
    print('sigin called')
    return render(request, 'registration/login.html')
