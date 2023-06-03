from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Delivery
from cart.models import Cart
from items.models import Item
from .forms import DeliveryForm

# Create your views here.

def delivery_total_price(request): 
    cart = list(Cart.objects.filter(user_id=request.user.id))[-1]
    items = Item.objects.filter(cart_id=cart.id)
    total = 0
    for item in items:
        total += int(item.amount) * int(item.dish.price)
    return total

@login_required(login_url="login")
def delivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST) 
        if form.is_valid():
                cart = list(Cart.objects.filter(user_id=request.user.id))[-1]
                new_delivery = Delivery(
                    order_id = cart,
                    address = form.cleaned_data['address'],
                    comment = form.cleaned_data['comment']
                )
                new_delivery.save()
                return redirect('delivery-details')     
    else: 
        form = DeliveryForm()
    return render(request,'delivery/before_delivery.html',{"form":form})


@login_required(login_url="login")
def delivery_details(request):
     total = delivery_total_price(request)
     cart = list(Cart.objects.filter(user_id=request.user.id))[-1]
     delivery_information = Delivery.objects.get(order_id=cart.id)
     return render(request,'delivery/delivery_details.html',{"delivery_information":delivery_information,"total":total})