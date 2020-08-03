from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .models import BuyersAuthentication
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegister

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        print(request.POST['email'])
        username = request.POST['email'].split("@")[0]
        password =  request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return HttpResponse('Success login')
    else:
        return render(request, 'authentication/login.html')

def signup(request):

    form = UserRegister()
    form = UserRegister(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            print('Your form data', form.cleaned_data)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            data = User.objects.create_user(first_name= name, username= username, email=email, password=password)
            data.save()
            user = authenticate(request, username= name, password=password)
            if user is not None:
                #login(request, user)
                pass
            else:
                HttpResponse('User wrong credentials')
            return redirect('/auth/loginUser')
        
    else:
        HttpResponse('404 Not found')
    return render(request, 'authentication/signup.html', {'form': form})

