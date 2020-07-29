from django.contrib import admin
from django.urls import path
from .views import home,products,customer,create_order,update_order,delete_order,register,loginPage,logoutUser

app_name = 'accounts'

urlpatterns = [

    path('register/',register,name='register'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    # path('user/',User,name='user'),
    path('',home,name='home'),
    path('products/',products,name='product'),
    path('customers/<str:pk_test>/',customer,name='customers'),
    path('create_order/<str:pk>/',create_order,name='create-order'),
    path('update_order/<str:pk>/', update_order,name='update_order'),
    path('delete_order/<str:pk>/', delete_order,name='delete_order')
]