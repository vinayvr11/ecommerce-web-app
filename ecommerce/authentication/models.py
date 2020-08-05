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


class Token(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    token = models.CharField(max_length=250, null=True)
    password = models.CharField(max_length=400, null=True)
