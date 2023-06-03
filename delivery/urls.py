from django.urls import path
from . import views

urlpatterns = [
    path('',views.delivery,name="delivery"),
    path('details',views.delivery_details,name="delivery-details")
]