from django.shortcuts import render, redirect
from django.core.mail import send_mail
import uuid
from .models import Seller, Token, Buyer
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def signupSeller(request):
    
    if request.method == 'GET':
        return render(request, 'seller-register.html')


def signupBuyer(request):
     if request.method == 'GET':
        return render(request, 'signup.html')   


def login(request, userType, token):
    if request.method == "GET":
        if token != 'none':
            get_token = Token.objects.get(token=token)
            print('Your token', get_token.name)
            if get_token is not None:
                if userType == 'seller':
                    seller = Seller(name=get_token.name, phone=get_token.phone, email=get_token.email, password=get_token.password,
                    address=get_token.address, businessaddress=get_token.businessaddress, 
                    productcategory=get_token.productcategory, display_picture=get_token.display_picture,
                    wallpaper=get_token.wallpaper,user_type=get_token.user_type)
                    seller.save()
                    get_token.delete()
                    return render(request, 'login.html')
                elif userType == "buyer":
                    buyer = Buyer(name=get_token.name, phone=get_token.phone, email=get_token.email, password=get_token.password, user_type=get_token.user_type)
                    buyer.save()
                    get_token.delete()
                    print('User data is saved')
                    return redirect('/')                   

        else:
            return render(request, 'login.html')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')


        buyer  = None
        seller = None
        if Seller.objects.exists():
            seller = Seller.objects.get(email=email)
        elif Buyer.objects.exists():
            buyer = Buyer.objects.get(email=email)

        else:    
            seller = Seller.objects.get(email=email)
            buyer = Buyer.objects.get(email=email)

            
        if seller is not None:

            if password == seller.password:
                request.session['is_login'] = True
                request.session['id'] = seller.email
                return redirect( '/sellers/profile')

            else:
                return render(request, 'login.html')
        elif buyer is not None:
            if password == seller.password:
                request.session['is_login'] = True
                request.session['id'] = buyer.email
                return redirect('/')
            else:
                return render(request, 'login.html')




#Email verification route

def authenticate(request, userType):
    if request.method == "GET":
        return render(request, 'signup.html')

    if request.method == "POST":

        token = str(uuid.uuid4())
        email = request.POST.get('email')
        print(email)
        send_mail(
            'Your verification email',
            'Here is your link- ' + "http://127.0.0.1:8000/auth/login/" + userType + "/" + token,
            email,
            [email],
            fail_silently=False
        )

        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        if userType == 'buyer':
            token = Token(name=name, password=password, email=email, token=token, phone=phone)
            token.save()  
            print('Token has been saved and sent')
            return redirect('/auth/signup-buyer')          
        elif userType == 'seller':
            address = request.POST.get('address')
            businessaddress = request.POST.get('businessaddress')
            productcategory = request.POST.get('productcategory')
            display_picture = request.FILES['display_pictures']
            wallpaper = request.FILES['wallpaper']
            user_type = userType
            token = Token(name=name, password=password, email=email, token=token, phone=phone,
            businessaddress=businessaddress, address=address, display_picture=display_picture, wallpaper=wallpaper, 
            user_type=user_type, productcategory=productcategory)
            token.save()
            print('Token has been saved and sent')
            return redirect('/auth/signup-seller')
        


def buyer(request):
    pass


def logout(request):
    if request.method == 'GET':
        request.session['id'] = None
        request.session['is_login'] = False
        return redirect('/')