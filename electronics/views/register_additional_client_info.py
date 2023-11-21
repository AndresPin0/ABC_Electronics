from django.shortcuts import render
from electronics.forms import *


def register_additional_information(request):
    form = MoreInformationForms()
    return render(request, 'additional_client_information.html', {'form': form})
