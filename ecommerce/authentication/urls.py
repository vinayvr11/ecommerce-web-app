
from django.urls import path
from . import views

urlpatterns = [
    path('login/<str:token>', views.login, name="login"),
    path('signup-seller', views.signup, name="signup"),
    path('authenticate', views.authenticate, name="authenticate")
]
