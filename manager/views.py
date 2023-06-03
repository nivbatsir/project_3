from django.shortcuts import render,redirect
from dish.models import Dish
from delivery.models import Delivery
from cart.models import Cart
from items.models import Item
from category.models import Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, DishForm
from django.contrib import messages
# Create your views here.

def category_name_not_unique(category_name):
    if Category.objects.filter(name=category_name):
        return True
    return False 


@login_required(login_url="login-manager")
def show_deliveries_not_deliver_yet(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    deliveries = Delivery.objects.all()
    return render(request,'manager/delivers_not_deliver_yet.html',{"deliveries":deliveries})


@login_required(login_url="login-manager")
def show_deliveries_history(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    deliveries = Delivery.objects.all()
    return render(request,'manager/deliveries_history.html',{"deliveries":deliveries[::-1]})



@login_required(login_url="login-manager")
def show_delivery_and_order(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    delivery = Delivery.objects.get(order_id=id)
    cart = Cart.objects.get(id=id)
    items = Item.objects.filter(cart_id=cart.id)
    total_raw_list = []
    total_sum = 0
    for item in items:
        total_sum += int(item.amount) * int(item.dish.price)
        total_raw_list.append(int(item.amount) * int(item.dish.price))
    items_and_total_raw_list = zip(items,total_raw_list)
    return render(request,'manager/order_and_delivery.html',
                  {"delivery":delivery,"items_and_total_raw_list":items_and_total_raw_list,"total_sum":total_sum})


@login_required(login_url="login-manager")
def is_delivered(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    delivery = Delivery.objects.get(order_id=id)
    if request.method == "POST":
        delivery.is_delivered = True
        delivery.save()
        return redirect('show-deliveries-history')


@login_required(login_url="login-manager")
def add_category(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            if category_name_not_unique(form.cleaned_data['name']):
                 messages.error(request,f"A category with that name already exists - {form.cleaned_data['name']}")
                 return redirect("add-category")
            new_category = Category(
                name = form.cleaned_data['name'],
                image = form.cleaned_data['image']
            )
            new_category.save()
            messages.success(request,f"New Category added - {form.cleaned_data['name']}")
            return redirect("show-manager-categories")
    else:
        form = CategoryForm()
    return render(request,"manager/add_category.html",{"form":form})



@login_required(login_url="login-manager")
def show_manager_categories(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    categories = Category.objects.all()
    return render(request,"manager/manager_categories.html",{"categories":categories})


@login_required(login_url="login-manager")
def delete_category(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')

    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.delete()
        return redirect('show-manager-categories')
    


@login_required(login_url="login-manager")
def edit_category(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            if category_name_not_unique(form.cleaned_data['name']):
                 messages.error(request,f"A category with that name already exists - {form.cleaned_data['name']}")
                 return redirect("edit-category",id = category.id)
            category.name = form.cleaned_data['name']
            category.image = form.cleaned_data['image']
            category.save()
            messages.success(request,f"Category edited successfully - {form.cleaned_data['name']}")
            return redirect("show-manager-categories")
    else:
        form = CategoryForm()
    return render(request,"manager/edit_category.html",{"form":form,"category":category})
    


@login_required(login_url="login-manager")
def show_manager_dishes(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    categories = Category.objects.all()
    return render(request,"manager/manager_dishes.html",{"categories":categories})


@login_required(login_url="login-manager")
def add_dish(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    categories = Category.objects.all()
    if request.method == "POST":
        is_gluten_free = request.POST.get('is_gluten_free') == 'on'
        is_vegeterian = request.POST.get('is_vegeterian') == 'on'
        if not request.POST.get('category_id'):
             messages.error(request,f"You must choose category to the new dish!")
             return redirect("add-dish")

        form = DishForm(request.POST)
        if form.is_valid():
            new_dish = Dish(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                image = form.cleaned_data['image'],
                is_gluten_free = is_gluten_free,
                is_vegeterian = is_vegeterian,
                category_id = request.POST['category_id']

            )
            new_dish.save()
            messages.success(request,f"New Dish added - {form.cleaned_data['name']}")
            return redirect("show-manager-dishes")
    else:
        form = DishForm()
    return render(request,"manager/add_dish.html",{"form":form,"categories":categories})



@login_required(login_url="login-manager")
def delete_dish(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')

    dish = Dish.objects.get(id=id)
    if request.method == "POST":
        dish.delete()
        return redirect('show-manager-dishes')
    


@login_required(login_url="login-manager")
def edit_dish(request,id):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('show-categories')
    
    dish = Dish.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == "POST":
        is_gluten_free = request.POST.get('is_gluten_free') == 'on'
        is_vegeterian = request.POST.get('is_vegeterian') == 'on'
        if not request.POST.get('category_id'):
             messages.error(request,f"You must choose category when you edit a dish!")
             return redirect("edit-dish",id=dish.id)
        form = DishForm(request.POST)
        if form.is_valid():
            dish.name = form.cleaned_data['name']
            dish.price = form.cleaned_data['price']
            dish.description = form.cleaned_data['description']
            dish.image = form.cleaned_data['image']
            dish.is_gluten_free = is_gluten_free
            dish.is_vegeterian = is_vegeterian
            dish.save()
            messages.success(request,f"Dish edited successfully - {form.cleaned_data['name']}")
            return redirect("show-manager-dishes")
    else:
        form = DishForm()
    return render(request,"manager/edit_dish.html",{"form":form,"dish":dish,"categories":categories})