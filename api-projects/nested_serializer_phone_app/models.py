from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.BigIntegerField()


class Order(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    customer = models.ForeignKey(
        Customer, related_name='books', on_delete=models.CASCADE)
