from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from items.models import Item
from cart.models import Cart

# Create your views here.


@login_required(login_url="login")
def add_dish_to_cart(request,id):
    if request.method == "POST":
        current_cart= list(Cart.objects.filter(user_id = request.user.id))[-1]
        new_item = Item(
            dish_id = id,
            cart_id = current_cart.id,
            amount = request.POST['amount']
        )
        new_item.save()
        return redirect('show-categories')

