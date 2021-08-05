from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=2090)
    image = models.ImageField(default = 'no-image.png', upload_to = 'services')
    detail = models.TextField(default='...no detail yet...')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    