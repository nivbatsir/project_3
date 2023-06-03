from django.db import models
from django.core.validators import MinValueValidator
from dish.models import Dish
from cart.models import Cart

# Create your models here.
class Item(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

