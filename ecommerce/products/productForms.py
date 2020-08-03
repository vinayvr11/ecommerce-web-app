from django import forms
from .models import ProductModel

class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product_name', 'product_description', 'product_price', 'product_shop_name',
                'product_shop_address', 'discount', 'category', 'product_image', 'product_rating']
    