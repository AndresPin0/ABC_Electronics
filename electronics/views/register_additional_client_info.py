from django.shortcuts import render
from electronics.forms import *
from datetime import datetime
from electronics.models import *
import traceback

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

            # aux_birthdate = datetime.strptime('2002-09-23', '%Y-%m-%d')
            # aux_gender = 'male'
            # aux_studying = True
            # aux_play_video_games = True
            # aux_platform = 'PC'

            additional_info = {
                'birth_place': {
                    'country': born_country,
                    'state': born_state,
                    'city': born_city
                },
                'living_place': {
                    'country': living_country,
                    'state': living_state,
                    'city': living_city,
                    'postal_code': postal_code
                },
                'hobbies': hobbies,
                'sports': sports,
                'marital_status': {
                    'status': marital_status,
                    'status_date_changed': marital_status_change_date,
                    'couple': {
                        'couple_name': couple_name
                    }
                },
                'category_interest': categories
            }

            additional_info_collection.insert_one(additional_info)
        

        except Exception as e:
            traceback.print_exc()
            print(f'Error: {e}')

    form = MoreInformationForms()
    return render(request, 'additional_client_information.html', {'form': form})
