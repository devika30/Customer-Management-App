from django.contrib import admin
from django.urls import path
from .views import home,products,customer

app_name = 'accounts'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='product'),
    path('customers/',customer,name='customer')
]