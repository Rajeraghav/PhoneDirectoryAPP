from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from LibraryManagementSystem import views
from django.contrib import admin
from django.urls import path, include



 


 
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
   
   
 
]

    
  

 

   
 
