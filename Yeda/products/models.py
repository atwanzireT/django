from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to = 'Products', default = 'no-image.png')
    price = models.FloatField(help_text='US DOLLARS $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created.strftime('%d/%m/%Y')}"
    
