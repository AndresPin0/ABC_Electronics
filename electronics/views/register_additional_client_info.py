from django.shortcuts import render, redirect
from electronics.models import *

def register_additional_information(request):
    return render(request, 'additional_client_information.html')