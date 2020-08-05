from django.db import models

# Create your models here.

class Order(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    product_id = models.CharField(max_length=400, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    user_address = models.CharField(max_length=250, blank=True)
    seller_id = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, blank=True)
    seller_address = models.CharField(max_length=400, blank=True)
    product_image = models.ImageField(upload_to="images/products", blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    is_packed = models.BooleanField(blank=True, null=True, default=False)
    is_delivered = models.BooleanField(blank=True, null=True, default=False)
    delivery_time = models.CharField(max_length=100, blank=True, null=True)
    order_place_time = models.CharField(max_length=100, blank=True)
