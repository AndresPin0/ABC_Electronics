from django.shortcuts import render, redirect
from electronics.forms import *


def register_additional_information(request):
    if request.method == 'POST':
        form = MoreInformationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('go-home')
    else:
        form = MoreInformationForms()
    return render(request, 'additional_client_information.html', {'form': form})
