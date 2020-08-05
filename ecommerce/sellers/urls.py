
from django.urls import path, include
from . import views


urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('register-product', views.registerProduct, name="registerProduct")
]
