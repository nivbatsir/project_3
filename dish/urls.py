from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.add_dish_to_cart,name="add-dish")
]