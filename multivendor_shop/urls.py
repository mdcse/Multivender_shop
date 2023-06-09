"""multivendor_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('master', master, name='master'),

    path('signup', signup, name='sign_up'),
    path('login', login, name='log_in'),
    path('account/', include('django.contrib.auth.urls')),

    #add to cart
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart_detail/',cart_detail,name='cart_detail'),

    # contact page
    path('contact_us/', contact_us, name='contact_us'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
