from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
import uuid

from authentication.models import Seller 

# Create your views here.

def profile(request):
    if request.method == "GET" and request.session['is_login'] == True:
        email = request.session['id']
        seller = Seller.objects.get(email= email)
        content = {"user_details": seller}
        return render(request, 'profile.html', content)
    else:
        return HttpResponse('Please login first')


def registerProduct(request):

    if request.method == "GET":
        return render(request, 'product-register.html')

    if request.method == "POST" and request.session['is_login'] == True:
        email = request.session['id']
        seller = Seller.objects.get(email=email)
        print("All fiels -------------======", request.FILES['im1'])

        prod_name = request.POST.get('prod_name')
        desc = request.POST.get('desc')
        category = request.POST.get('category')
        for_whom = request.POST.get('for_whom')
        before_price = request.POST.get('before_price')
        after_price = request.POST.get('after_price')
        quantity = request.POST.get('quantity')
        im1 = request.FILES['im1']
        im2 = request.FILES['im2']
        im3 = request.FILES['im3']
        im4 = request.FILES['im4']
        im5 = request.FILES['im5']
        product_id = uuid.uuid4()

        product = Product(user_id=email, username=seller.name, prod_name=prod_name,
        desc=desc, category=category, for_whom=for_whom, before_price=before_price,
        after_price=after_price, quantity=quantity, im1=im1, im2=im2, im3=im3, 
        im4=im4, im5=im5, left=quantity, product_id=product_id)

        product.save()

        return render(request, 'product-register.html')
    else:
        return redirect('/auth/login')



