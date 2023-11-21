from django.shortcuts import render, redirect
from electronics.models import *

def buy_product(request):
    return render(request, 'buy_product.html')