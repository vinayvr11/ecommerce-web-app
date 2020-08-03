# Generated by Django 3.0.8 on 2020-08-03 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_productmodel_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_pub_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
