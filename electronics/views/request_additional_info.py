from django.shortcuts import render, redirect
from electronics.models import *
from electronics.views import home


def request_additional_client_information(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('selected-product-id', '')

            print(product_id)

            return render(request, 'request_additional_information.html', {
                'product_id': product_id
            })
        
        except Exception as e:
            print(f'Error: {e}')
            
            return redirect(home.home)

    return redirect(home.home)


def manage_answer(request):
    if request.method == 'POST':
        try:
            answer = request.POST.get('answer', '')

            product_id = request.POST.get('selected-product-id', '')

            if answer == 'Sí':
                return render(request, 'additional_client_information.html', {
                    'product_id': product_id
                })
            else:
                return render(request, 'neccessary_client_information.html', {
                    'product_id': product_id
                })
            
        except Exception as e:
            print(f'Error: {e}')

            return redirect(home.home)
