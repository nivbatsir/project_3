from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from items.models import Item

# Create your views here.

def is_cart_empty(request):
    cart = list(Cart.objects.filter(user_id=request.user.id))[-1]
    items = Item.objects.filter(cart_id=cart.id)
    return len(items) == 0


@login_required(login_url="login")
def new_cart(request):
    new_cart = Cart(
        user_id = request.user.id
    )
    new_cart.save()
    return redirect('show-categories')


@login_required(login_url="login")
def show_cart(request):
    cart = list(Cart.objects.filter(user_id=request.user.id))[-1]
    items = Item.objects.filter(cart_id=cart.id)
    empty = is_cart_empty(request)
    total_raw_list = []
    total_sum = 0
    for item in items:
        total_sum += int(item.amount) * int(item.dish.price)
        total_raw_list.append(int(item.amount) * int(item.dish.price))
    items_and_total_raw_list = zip(items,total_raw_list)
    return render(request,'cart/show_cart.html',{"items_and_total_raw_list":items_and_total_raw_list,"total_sum":total_sum,"is_cart_empty": empty})


@login_required(login_url="login")
def show_carts_history(request):
    carts = list(Cart.objects.filter(user_id=request.user.id))[:-1]
    delivery_date_list = []
    delivery_success_list = []
    carts_with_history = []
    sum_list = []
    for current_cart in carts:
        items = Item.objects.filter(cart_id=current_cart.id)
        if len(items) == 0:
            continue
        else:
            delivery_date_list.append(current_cart.delivery.created)
            delivery_success_list.append(int(current_cart.delivery.is_delivered) == 1)
            carts_with_history.append(current_cart)
            items = Item.objects.filter(cart_id=current_cart.id)
            total = 0
            for item in items:
                total += int(item.amount) * int(item.dish.price)
            sum_list.append(total)
    if len(carts_with_history) == 0:
        return render(request,'cart/show_carts_history.html',{"non_carts_history": True})
    else:
        history_sum_date_success_lists = zip(carts_with_history[::-1],sum_list[::-1],delivery_date_list[::-1],delivery_success_list[::-1])
        return render(request,'cart/show_carts_history.html',
                    {"history_sum_date_success_lists":history_sum_date_success_lists})


@login_required(login_url="login")
def remove_item_from_cart(request,id):
    if request.method == "POST":
        item = Item.objects.get(id=id)
        item.delete()
        return redirect("show-cart")


