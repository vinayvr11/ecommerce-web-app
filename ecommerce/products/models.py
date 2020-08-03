from django.db import models
from datetime import date
# Create your models here.
class ProductModel(models.Model):
    product_id = models.AutoField
    product_pub_date = models.DateField(("Date"), default=date.today)
    seller_id = models.AutoField
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=3000,  default="")
    product_rating = models.IntegerField(default=0)
    product_price = models.BigIntegerField(default=0)
    product_shop_name = models.CharField(max_length=500,  default="")
    product_shop_address = models.CharField(max_length=600,  default="")
    discount = models.IntegerField(default=0)
    category = models.CharField(max_length=300,  default="")
    product_image = models.ImageField(upload_to='products/images', default="")

    def __str__(self):
        return self.product_name