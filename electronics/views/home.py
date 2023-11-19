from django.shortcuts import render, redirect
from electronics.models import *

def home(request):
    products = Product.objects.all()

    render(request, 'home.html', {
        "products": products
    })