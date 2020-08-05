from django.shortcuts import render

# Create your views here.

def profile(request):
    
    if request.method == "GET":
        return render(request, 'profile.html')