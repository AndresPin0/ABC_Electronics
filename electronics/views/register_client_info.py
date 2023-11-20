from django.shortcuts import render, redirect
from electronics.models import *
from electronics.views import home
from datetime import datetime
from django.db import transaction


def register_client_information(request):
    print('AAAAAAAAAAAAAAAAAAAAAAAH')

    if request.method == 'POST':
        result_message = ''

        try:
            customer_id = request.POST.get('customer-id', '')
            product_id = request.POST.get('selected-product-id', '')
            
            product = Product.objects.get(product_id=product_id)

            print(f'Product ID: {product_id}')

            data = {
                'firstname': request.POST.get('customer-firstname', ''),
                'lastname': request.POST.get('customer-lastname', ''),
                'address': request.POST.get('customer-address', ''),
                'date_of_birth': request.POST.get('customer-birthDate', ''),
                'email': request.POST.get('customer-email', ''),
                'home_phone': request.POST.get('customer-homePhone', ''),
                'cell_phone': request.POST.get('customer-cellPhone', '')
            }

            with transaction.atomic():
                customer, created = Customer.objects.update_or_create(customer_id=customer_id, defaults=data)

                new_order = Order.objects.create(customer_id=customer,
                                                order_date=datetime.now(),
                                                shipped_date=datetime.now(),
                                                payment_date=datetime.now())
                
                new_order.save()

                new_order_details = OrderDetail.objects.create(order_number=new_order,
                                                            product_id=product)
                
                new_order_details.save()

                product.quantity_available -= 1
                product.save()

                result_message = 'Orden creada exitosamente'

        except Exception as e:
            print(f'Error: {e}')

            result_message = 'Error al crear la orden'

        return render(request, 'neccessary_client_information.html', {
            'result_message': result_message
        })

    return render(request, 'neccessary_client_information.html')