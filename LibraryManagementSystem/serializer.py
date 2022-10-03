from rest_framework import serializers
from .models import *
from .forms import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CartBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartBooks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    is_customer = User.user
    is_admin = User.admin
    class Meta:
        model = SignUpForm
        fields = ('username', 'email','is_customer','is_admin')

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =addUser
        fields = '__all__'


class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpForm
        fields = ('username', 'email', 'password1', 'password2')
        extra_kwargs = {
            'password1':{'write_only': True}
        }
    def save(self, **kwargs):
        user = User(
            username = self.validated_data['user'],
            email = self.validated_data['email'],
        )
        password1 = self.validated_data['password1'],
        password2 = self.validated_data['password2'],
        if password1 != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password1)
        user.is_admin = True
        user.save()
        return user

class ClientSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpForm
        fields = ('username', 'email', 'password1', 'password2')
        extra_kwargs = {
            'password1':{'write_only': True}
        }