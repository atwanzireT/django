from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(default="...No Description...")
    image_urls = models.CharField(max_length=2090)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name

class Headline(models.Model):
    topic = models.CharField(max_length=50)
    author = models.CharField(max_length = 50, default="Fedora")
    image = models.ImageField(upload_to = 'home', default = 'no-image.png')
    category_name = models.ManyToManyField(Category)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.topic  