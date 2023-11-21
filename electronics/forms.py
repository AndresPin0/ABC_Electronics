from django import forms
from .models import MoreInformation


class MoreInformationForms(forms.ModelForm):
    class Meta:
        model = MoreInformation
        fields = '__all__'