
from django.urls import path
from . import views

urlpatterns = [
    path('register-products', views.register_product, name="register_product"),
    path('get-products', views.get_product, name="get_product")
]
