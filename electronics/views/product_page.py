from django.shortcuts import render, redirect
from electronics.models import *
from electronics.views import home

def product_page(request):
    try:
        if request.method == 'POST':
            product_id = request.POST.get('selected-product-id', '')
            product = Product.objects.get(product_id=product_id)

            return render(request, 'product_page.html', {
                'product': product
            })

    except Exception as e:
        print(f'Error: {e}')

        return redirect(home.home)
