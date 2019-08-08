from django.db import models

# Create your models here.

class Destination(models.Model):
    #id = 0
    name = models.CharField(max_length=100)
    description = models.TextField()
    offer = models.BooleanField(default=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')