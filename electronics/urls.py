from django.urls import path
from .views import register_additional_client_info, home, product_page, buy_product, request_additional_info, register_client_info, list_current_orders

urlpatterns = [
    path('', home.home, name='base'),
    path('home/', home.home, name='go-home'),
    path('registerAdditionalInfo/', register_additional_client_info.register_additional_information, name='register-additional-info'),
    path('productPage/', product_page.product_page, name='product-page'),
    path('buyProduct/', buy_product.buy_product, name='buy-product'),
    path('requestAdditionalInfo/', request_additional_info.request_additional_client_information, name='request-addtional-information'),
    path('manageRequestInfoAnswer/', request_additional_info.manage_answer, name='manage-answer'),
    path('registerCustomerInformation/', register_client_info.register_client_information, name='register-client-info'),
    path('listCurrentOrders/', list_current_orders.list_orders, name='list-of-orders'),

]