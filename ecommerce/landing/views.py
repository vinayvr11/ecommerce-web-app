from django.shortcuts import render
from authentication.models import Buyer, Seller
from sellers.models import Product
from .models import Order
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def order(request):
    if request.method == "GET":
        return render(request, 'order.html')
    if request.method == "POST":
        
        seller_email = request.POST.get('email')
       
        seller = Seller.objects.get(email=seller_email)
        product = None
        if Product.objects.exists():
            product = Product.objects.filter(user_id=seller_email).values()[0]
            
        print("Dict object", product)
        category = product['category']    
        product_id = product['product_id']
        seller_address = seller.businessaddress
        user_email = request.POST.get('useremail')
        price = request.POST.get('useremail')
        user_address = request.POST.get('user_address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')
        
        product_image = product['im1']
        order_place_time = datetime.datetime.now()
        

        order = Order(seller_address=seller_address, seller_id=seller_email, email=user_email, 
        quantity=quantity, phone=phone, user_address=user_address, price=price, product_id=product_id,
        category=category, product_image=product_image, order_place_time=order_place_time)
        order.save()
        return HttpResponse('Product placed')


def search(request):
    if request.method == "POST":
        item = request.POST.get('search')
        print("Your item", item)
        return HttpResponse('We have search your item')