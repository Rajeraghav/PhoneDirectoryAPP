
from django.db import models

class Userreg(models.Model):
    id=models.AutoField(primary_key=True)
    usertype=models.CharField(max_length=70, blank=False, default='')
    username=models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    mobilenumber=models.CharField(max_length=70, blank=False, default='')
    password= models.CharField(max_length=50,blank=False, default='')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    

