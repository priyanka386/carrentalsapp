from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name= models.CharField(max_length=100)
    price = models.IntegerField()
    # type = models.CharField(max_length=150)
    image = models.ImageField(upload_to='')

class Orders(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE, blank=True, null=True)
    payment_status = models.BooleanField(default=False)


class AddCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE, blank=True, null=True)
    grand_total = models.IntegerField(default=0)












