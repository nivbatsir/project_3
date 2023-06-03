from django.urls import path
from . import views

urlpatterns = [
    path('current',views.show_cart,name="show-cart"),
    path("history",views.show_carts_history,name="show-carts-history"),
    path('new',views.new_cart,name="new-cart"),
    path('remove/<int:id>',views.remove_item_from_cart,name="remove-item")
]