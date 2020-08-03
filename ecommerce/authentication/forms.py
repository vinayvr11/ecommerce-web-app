from django import forms
from django.contrib.auth.models import User
from django.db import models

class UserRegister(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)



    