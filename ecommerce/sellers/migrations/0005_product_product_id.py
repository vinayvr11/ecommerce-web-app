# Generated by Django 3.0.8 on 2020-08-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0004_product_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]