from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_categories,name="show-categories"),
    path('<str:category_name>',views.show_category,name="show-category")
]