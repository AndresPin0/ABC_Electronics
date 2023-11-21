from django.shortcuts import render
from electronics.forms import *


def register_additional_information(request):
    if request.method == 'POST':
        try:
            born_country = request.POST.get('born-country', '')
            born_state = request.POST.get('born-state', '')
            born_city = request.POST.get('born-city', '')
            living_country = request.POST.get('living-country', '')
            living_state = request.POST.get('living-state', '')
            living_city = request.POST.get('living-city', '')
            postal_code = request.POST.get('postal-code', '')
            hobbies = request.POST.getlist('hobbies[]', default=[])
            sports = request.POST.getlist('sports[]', default=[])
            marital_status = request.POST.get('marital-status', '')
            marital_status_change_date = request.POST.get('marital-change-date', '')
            couple_name = request.POST.get('couple-name', '')
            categories = request.POST.getlist('categories[]', default=[])

            

        except Exception as e:
            print(f'Error: {e}')

    form = MoreInformationForms()
    return render(request, 'additional_client_information.html', {'form': form})
