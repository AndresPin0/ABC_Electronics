from django.shortcuts import render
from electronics.forms import *


def register_additional_information(request):
    form = hobbiesForm()
    form1 = ChildForm()
    form2 = BirthPlaceForm()
    return render(request, 'additional_client_information.html', {'form': form, 'form1': form1, 'form2': form2})
