from django.db import models
from cart.models import Cart

# Create your models here.
class Delivery(models.Model):
    order_id = models.OneToOneField(Cart,on_delete=models.CASCADE,primary_key=True)
    is_delivered = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.order_id