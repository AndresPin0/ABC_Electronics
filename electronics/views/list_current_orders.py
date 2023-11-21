from django.shortcuts import render, redirect
from electronics.models import *
from electronics.views import home

def list_orders(request):
    if request.method == 'POST':
        try:
            customer_id = request.POST.get('customer-id', '')
            customer = Customer.objects.get(customer_id=customer_id)

            orders = Order.objects.filter(customer_id=customer)

            order_details = OrderDetail.objects.filter(order_number__in=orders)

            return render(request, 'current_orders.html', {
                'filtered_orders': orders,
                'order_details': order_details
            })

        except Exception as e:
            print(f'Error: {e}')
        
    return render(request, 'current_orders.html')