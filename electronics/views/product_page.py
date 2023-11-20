from django.shortcuts import render, redirect
from electronics.models import *
from electronics.views import home

def product_page(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('selected-product-id', '')
            product = Product.objects.get(product_id=product_id)

            return render(request, 'product_page.html', {
                'product': product
            })
        except Exception as e:
            return redirect(home.home)
        
    return redirect(home.home)