from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    businessaddress = models.CharField(max_length=400, null=True, blank=True)
    password = models.CharField(max_length=400, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    productcategory = models.CharField(max_length=100, null=True, blank=True)
    display_picture = models.ImageField(upload_to="images/products", blank=True)
    wallpaper = models.ImageField(upload_to="images/products", blank=True)
    user_type = models.CharField(max_length=20, default='', blank=True, null=True)


class Token(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    businessaddress = models.CharField(max_length=400, null=True, blank=True)
    password = models.CharField(max_length=400, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    productcategory = models.CharField(max_length=100, null=True, blank=True)
    display_picture = models.ImageField(upload_to="images/products", blank=True)
    wallpaper = models.ImageField(upload_to="images/products", blank=True)
    user_type = models.CharField(max_length=20, default='', blank=True, null=True)
    token = models.CharField(max_length=250, null=True)


class Buyer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=60 ,blank=True, null=True)
    password = models.CharField(max_length=400, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=30, blank=True, null=True)