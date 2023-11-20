from django.shortcuts import render, redirect
from electronics.models import *
from electronics.forms import *


def register_additional_information(request):

    if request.method == 'POST':
        gender = request.POST.getlist('gender')
        hobbies = request.POST.getlist('hobbies')

    else:
        form = hobbiesForm()
    return render(request, 'additional_client_information.html', {'form': form})