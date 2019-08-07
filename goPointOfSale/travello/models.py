from django.db import models

# Create your models here.

class Destination:
    #id = 0
    name = " "
    description = " "
    offer = False
    price = 100
    image = " "
    def __init__(self, name, desc, offer, price, image):
        self.name= name
        self.desc=desc
        self.offer=offer
        self.price=price
        self.image=image