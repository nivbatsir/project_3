from django.urls import path
from . import views

urlpatterns = [
    path("deliveries",views.show_deliveries_not_deliver_yet,name="show-deliveries-not-deliver-yet"),
    path("deliveries_hitory",views.show_deliveries_history,name="show-deliveries-history"),
    path("delivery_and_order/<int:id>",views.show_delivery_and_order,name="show-delivery-and-order"),
    path("is_delivered/<int:id>",views.is_delivered,name="is-delivered"),
    path("add_category",views.add_category,name="add-category"),
    path("categories",views.show_manager_categories,name="show-manager-categories"),
    path("edit_category/<int:id>",views.edit_category,name="edit-category"),
    path("delete_category/<int:id>",views.delete_category,name="delete-category"),
    path("dishes",views.show_manager_dishes,name="show-manager-dishes"),
    path("add_dish",views.add_dish,name="add-dish"),
    path("edit_dish/<int:id>",views.edit_dish,name="edit-dish"),
    path("delete_dish/<int:id>",views.delete_dish,name="delete-dish")
]