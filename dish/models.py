from django.db import models
from django.core.validators import MinValueValidator
from category.models import Category

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    is_gluten_free = models.BooleanField()
    is_vegeterian = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
