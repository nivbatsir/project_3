from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.TextField()


    def __str__(self):
        return self.name