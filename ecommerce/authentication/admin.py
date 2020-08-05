from django.contrib import admin
from .models import Seller, Token, Buyer

# Register your models here.
admin.site.register(Seller)
admin.site.register(Token)
admin.site.register(Buyer)