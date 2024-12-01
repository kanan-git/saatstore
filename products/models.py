from django.db import models

# from ..accounts.models import Profile

class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=16)
    category = models.CharField(max_length=16)
    description = models.TextField()
    price = models.FloatField()
    availability = models.BooleanField()
    # store = Profile.store_name


    def __str__(self):
        return f'{self.brand} {self.title} {self.category} - ${self.price}USD | {self.availability}'
