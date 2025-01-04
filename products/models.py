from django.db import models
from django.contrib.auth.models import User

# models.OneToOneField() - x2x
# models.ForeignKey() - x2n
# models.ManyToMany() - n2n


class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=16)
    category = models.CharField(max_length=16)
    description = models.TextField()
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    # image_path = models.ImageField(upload_to='media', null=True, blank=True)
    image_path = 'https://picsum.photos/200'
    store = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.brand} {self.title} {self.category} - ${self.price}USD | {self.availability}'
