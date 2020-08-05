
from django.urls import path
from . import views

urlpatterns = [
    path('login/<str:userType>/<str:token>', views.login, name="login"),
    path('signup-seller', views.signup, name="signup"),
    path('signup-buyer', view.buyer, name="buyer"),
    path('authenticate/<str:userType>', views.authenticate, name="authenticate"),
    path('logout', views.logout, name="logout")
]
