from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ItemSize(models.Model):
    size = models.CharField(max_length=15)
    pct_of_price = models.IntegerField()

    def __str__(self):
        return f"{self.size}"


class Toppings(models.Model):
    topping_type = models.CharField(max_length=10)
    topping = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)


class Menu(models.Model):
    item = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.item}"


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    cart = models.ManyToManyField(Menu, blank=True, related_name="cart")

    def __str__(self):
        return f"{self.address}"
