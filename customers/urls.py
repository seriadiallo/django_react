from django.urls import path

from .views import  customers_list, customers_detail

urlpatterns = [
    path('customers/', customers_list),
    path('customers/<int:pk>/', customers_detail)
]