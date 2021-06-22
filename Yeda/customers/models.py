from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=80)
    logo = models.ImageField(default='no-image.png', upload_to='customers')

    def __str__(self):
        return str(self.name)
