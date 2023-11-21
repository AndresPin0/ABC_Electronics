from django.urls import path
from .views import register_additional_client_info, home, product_page

urlpatterns = [
    path('', home.home, name='base'),
    path('home/', home.home, name='go-home'),
    path('registerAdditionalInfo/', register_additional_client_info.register_additional_information, name='registerAdditionalInfo'),
    path('productPage/', product_page.product_page, name='product-page'),
]