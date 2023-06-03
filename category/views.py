from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category
from cart.views import is_cart_empty

# Create your views here.

@login_required(login_url="login")
def show_categories(request):
    categories = Category.objects.all()
    return render(request,'category/categories.html',{"categories":categories,"is_cart_empty": is_cart_empty(request)})

@login_required(login_url="login")
def show_category(request,category_name):
    category = Category.objects.get(name=category_name)
    return render(request,'category/category.html',{"dishes":category.dish_set.all(),"category":category,"is_cart_empty": is_cart_empty(request)})