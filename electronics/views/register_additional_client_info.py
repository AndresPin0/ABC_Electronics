# from django.shortcuts import render, redirect
# from electronics.models import *
# from django.views.generic import TemplateView
# from django.shortcuts import render
# from electronics.forms import ChildForm, LocationForm, MaritalStatusForm, ClientForm


# class AdditionalInformationView(TemplateView):
#     template_name = 'additional_client_information.html'

    # def add_information(self, request):
    #     # client = ClientForm()
    #     # return render(request, self.template_name, {'form': client})
    #     return render(request, 'additional_client_information.html')

from django.shortcuts import render, redirect
from electronics.models import *

def register_additional_information(request):
    return render(request, 'additional_client_information.html')