from django.db import models
from django.contrib.auth.models import User
from blog.models import Category

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    Category_interest = models.ManyToManyField(Category, on_delete = models.CASCADE)
    bio = models.TextField(default='...no bio ...')
    interest = models.TextField(default='...no interests yet...')
    avater = models.ImageField(default='no-image.png', upload_to='Profiles')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.username 
    
