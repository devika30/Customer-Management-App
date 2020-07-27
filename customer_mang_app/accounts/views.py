from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    context={
        'orders':orders,
        'customers':customers
    }
    return render(request,'accounts/dashboard.html',context)

def customer(request):
    return render(request,'accounts/customer.html')


def products(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'accounts/products.html',context)
