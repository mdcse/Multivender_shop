from django.shortcuts import render, redirect
from app.models import Category, Product

from django.contrib.auth import authenticate, login
from app.models import UserCreateForm

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

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

def login(request):
    print('sigin called')
    return render(request, 'registration/login.html')

<<<<<<< HEAD

=======
# add to cart
>>>>>>> 8b8e9537ba4bc6518213abbfd08f4ca1f35a3e30

@login_required(login_url="/account/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
<<<<<<< HEAD
    print(cart)
=======
>>>>>>> 8b8e9537ba4bc6518213abbfd08f4ca1f35a3e30
    return redirect("index")


@login_required(login_url="/account/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
