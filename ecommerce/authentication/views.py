from django.shortcuts import render, redirect
from django.core.mail import send_mail
import uuid
from .models import Seller, Token
from django.http import HttpResponse

# Create your views here.

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        pass


def login(request, token):
    if request.method == "GET":
        if token != 'none':
            get_token = Token.objects.get(token=token)
            print('Your token', get_token.name)
            if get_token is not None:
                seller = Seller(name=get_token.name, phone=get_token.phone, email=get_token.email, password=get_token.password)
                seller.save()
                get_token.delete()
                print('User data is saved')
                return HttpResponse('User data has been saved')
        else:
            return render(request, 'login.html')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Seller.objects.get(email=email)
        if user is not None:
            request.session['is_login'] = True
            request.session['user'] = user
            
            seller = Seller(email=email)

            return HttpResponse('Login sucessfully')

def authenticate(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    if request.method == "POST":

        token = str(uuid.uuid4())
        email = request.POST.get('email')
        send_mail(
            'Your verification email',
            'Here is your link- ' + "http://127.0.0.1:8000/auth/login/" + token,
            email,
            ['vr54640@gmail.com'],
            fail_silently=False
        )

        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        token = Token(name=name, password=password, email=email, token=token, phone=phone)
        token.save()

        print('Token has been saved and sent')
        return redirect('/auth/signup-seller')