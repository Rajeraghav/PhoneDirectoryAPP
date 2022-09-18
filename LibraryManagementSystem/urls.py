from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from LibraryManagementSystem import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from . import views


 


 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginaction, name ='login'),
    path('signup/', views.signaction, name ='signup'),
    url(r'^users$',views.usersApi),
    url(r'^users/([?P<pk>0-9]+)$',views.usersApi),
    url(r'^admins$',views.adminsApi),
    url(r'^admins/([?P<pk>0-9]+)$',views.adminsApi),
     path('grid/', views.grid, name='gridadd'),
    path('add_book/', views.addbooks, name='add_book'),
    path('edit_book/',views.editbooks, name='edit_book'),
    path('payment_details/',views.payments, name='payment_details'),
    
   
 
]

    
  

 

   
 
