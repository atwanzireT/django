from django.db import models
from django.db.models.deletion import CASCADE
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code


# ############## Sales Models ####################### #
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True, help_text="This is automatically Filled")
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id: IT0{self.id}       Product: {self.product}         Quantity: {self.quantity}       Price: {self.price}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True, help_text='This is generated automatically')
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null = True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now
        return super().save(*args, **kwargs)

    def get_position(self):
        return self.positions.all()

    def __str__(self):
        return f"The sales of amount ${self.total_price}"


class CSV(models.Model):
    file_name = models.FileField(upload_to='cvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
