from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

# Create your models here.

choice = (('admin','admin'),('user','user'))
class User(AbstractUser):
    adminORuser = models.CharField(max_length=10,choices=choice)
    email = models.CharField(max_length=100, unique=True, null=True, blank=True)
    username = models.CharField(null=True, unique=True, max_length=100, blank=True)
    mobileNumber = models.CharField(null=True, blank=True, max_length=10)
    password1 = models.CharField(null=True, blank=True, max_length=100)
    password2 = models.CharField(null=True, blank=True, max_length=100)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Book(models.Model):
    enterId = models.IntegerField(null=True,unique=True, blank=True)
    enterName = models.CharField(max_length=100, null=True, blank=True)
    enterAuthorName = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.enterName

class PaymentDetails(models.Model):
    cartNumber = models.IntegerField(null=True, blank=True)
    enterCcv = models.IntegerField(null=True, blank=True)
    enterPhoneNumber = models.IntegerField(null=True, blank=True)
    getBook = models.IntegerField(null=True, blank=True)
    enterDays = models.IntegerField(null=True, blank=True)

class cartBooks(models.Model):
    enterId = models.IntegerField(null=True, unique=True, blank=True)
    enterName = models.CharField(max_length=100, null=True, blank=True)
    enterAuthorName = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.id

'''
class addUser(models.Model):
    admin = models.BooleanField('Is admin', default=False)
    user = models.BooleanField('Is user', default=False)
    email = models.CharField(max_length=100, unique=True,null=True, blank=True)
    username = models.CharField(null=True, max_length=100,blank=True)
    mobileNumber = models.IntegerField(null=True, blank=True)
    password1 = models.CharField(null=True, blank=True, max_length=100)
    password2 = models.CharField(null=True, blank=True, max_length=100)
'''