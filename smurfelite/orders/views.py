from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, 'users/profile.html')

def cart(request):
    return render(request, "orders/cart.html")

def checkout(request):
    return render(request, "orders/checkout.html")