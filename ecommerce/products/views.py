from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel
import datetime
from products.productForms import ProductForms

# Create your views here.
def register_product(request):
    form  = ProductForms
    if request.method == 'POST':
        print('Your files--------------', request.FILES)
        data = ProductForms(request.POST, request.FILES)
        if data.is_valid:
            data.save()
            HttpResponse('Product data have been saved')
              
    else:
        HttpResponse('Request has been changed')
        
    return render(request, 'products/product_register.html', {'form': form}) 

def get_product(request):
    print(ProductModel.objects.all())
    return HttpResponse('Get all products')
