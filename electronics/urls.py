from django.urls import path

from .views import register_additional_client_info

urlpatterns = [
    path('registerAdditionalInfo/', register_additional_client_info.register_additional_information, name='register-additional-info'),

]