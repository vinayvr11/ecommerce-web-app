from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.


fs = FileSystemStorage(location='/static/images/product')

class Product(models.Model):

    id = models.AutoField
    username = models.CharField(max_length=30, blank=True, null=True)
    prod_name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    for_whom = models.CharField(max_length=10, blank=True, null=True)
    before_price = models.IntegerField
    after_price = models.IntegerField
    quantity = models.IntegerField
    left = models.IntegerField
    im1 = models.ImageField(upload_to="images/products", default="", blank=True, null=True)
    im2 = models.ImageField(upload_to="images/products", default="", blank=True, null=True)
    im3 = models.ImageField(upload_to="images/products", default="", blank=True, null=True)
    im4 = models.ImageField(upload_to="images/products", default="", blank=True, null=True)
    im5 = models.ImageField(upload_to="images/products", default="", blank=True, null=True)

    def __str__(self):
        return str(self.id)



