from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Inventory(models.Model):
    item = models.CharField(max_length=20)
    item_code = models.IntegerField()
    item_condition = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return self.item


class Order(models.Model):
    ord_number = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    ordered_by = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.ord_number

# signals
from django.db.models.signals import pre_save
def validate_Order(sender, instance, **kwargs):
    if instance.quantity < instance.Inventory.quantity:
        instance.save()
    else:
        print("Instance can not be saved")
    pre_save(validate_Order, sender = Order)

# notify User
