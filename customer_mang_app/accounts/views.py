from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@unauthenticated_user
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ user)
        return redirect('accounts:login')
    context={
        'form':form
    }
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect( 'accounts:home')

        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request,'accounts/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')

@login_required(login_url='accounts:login')
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_orders=orders.count()
    total_customers=customers.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'total_customers':total_customers,
        'delivered':delivered,
        'pending':pending
    }
    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='accounts:login')
def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    order=customer.order_set.all()
    total_orders=order.count()
    myFilter=OrderFilter(request.GET,queryset=order)
    order=myFilter.qs
    context={
        'customer':customer,
        'order':order,
        'total_orders':total_orders,
        'myFilter':myFilter
    }
    return render(request,'accounts/customer.html',context)


@login_required(login_url='accounts:login')
def products(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'accounts/products.html',context)

@login_required(login_url='accounts:login')
def create_order(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    form = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form} 
    return render(request, 'accounts/orders.html', context)

@login_required(login_url='accounts:login')
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
        }
    return render(request, 'accounts/orders.html', context)

@login_required(login_url='accounts:login')
def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={
        'item':order
    }
    return render(request,'accounts/delete.html',context)