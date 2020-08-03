from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BuyersAuthentication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    full_name = models.CharField(max_length=40, default="")
    address = models.CharField(max_length=40, default="")
    phone = models.CharField(max_length=14, default="")
    

class UserSeller(models.Model):
    seller_id = models.AutoField
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    location = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=15, default="")
    shop_name = models.CharField(max_length=200, default="")