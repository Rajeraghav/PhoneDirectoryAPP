from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}) )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    mobileNumber = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))


    class Meta:
        model = User
        fields = ('admin', 'user','email','username', 'mobileNumber', 'password1', 'password2' )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('enterId', 'enterName', 'enterAuthorName', 'price')

class addUserForm(forms.ModelForm):
    class Meta:
        model = addUser
        fields = '__all__'

class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class cartBookForm(forms.ModelForm):
    class Meta:
        model = cartBooks
        fields = '__all__'

