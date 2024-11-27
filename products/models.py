from django.db import models

class Product():
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=16)
    category = models.CharField(max_length=16)
    description = models.TextField()
    price = models.FloatField()
    availability = models.BooleanField()

    def __str__(self):
        return self.brand + " " + self.title + " " + self.category + " " + self.price
