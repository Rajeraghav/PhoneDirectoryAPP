from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('adminORuser','email','username', 'mobileNumber', 'password1', 'password2')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('enterId', 'enterName', 'enterAuthorName', 'price')

class addUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('adminORuser','email','username', 'mobileNumber', 'password1', 'password2')

class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class cartBookForm(forms.ModelForm):
    class Meta:
        model = cartBooks
        fields = '__all__'

