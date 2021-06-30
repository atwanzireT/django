from django.db import models
from profiles.models import Profile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='category', default='no-image.png')
    description = models.TextField(default='...no description...')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Supplier')
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', default='no_image.png')
    description = models.TextField(default='...no description...')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

