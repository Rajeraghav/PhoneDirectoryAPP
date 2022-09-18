
from django.db import models

# Create your models here.

#New User Table
 
class Newuser(models.Model):
    usertype=models.CharField(max_length=70, blank=False, default='')
    username=models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    mobilenumber=models.CharField(max_length=70, blank=False, default='')
    password= models.CharField(max_length=50,blank=False, default='')
    confirmpassword= models.CharField(max_length=50,blank=False, default='')
    class Meta:
        db_table="Newuser"
 



    
    
    
    


   