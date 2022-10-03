from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from .forms import SignUpForm, LoginForm, BookForm
from django.contrib.auth import login, authenticate
from .models import *
from .serializer import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('LibraryManagementSystem:login-view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.admin:
                login(request, user)
                return redirect('LibraryManagementSystem:adminpage')
            elif user is not None and user.user:
                login(request, user)
                return redirect('LibraryManagementSystem:customer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
def customer(request,id=0):
    msg = None
    form = PaymentDetailsForm()
    bookinfo = Book.objects.all()
    if request.method == "POST":
        if id ==0:
            form = PaymentDetailsForm(request.POST)
        else:
            payment = PaymentDetailsForm.objects.get(pk=id)
            form = PaymentDetailsForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            msg = 'Payment is Done'
            return redirect('LibraryManagementSystem:customer')
        else:
            msg = 'Payment is not Done'
            return redirect('LibraryManagementSystem:customer')
    else:
        if id==0:
            form = PaymentDetailsForm()
        else:
            book = PaymentDetails.objects.get(pk=id)
            form = PaymentDetailsForm(request.POST,instance=book)
    return render(request, 'customer.html', {'form': form, 'msg': msg, 'bookinfo': bookinfo})
def getBook(request,id):
    book = Book.objects.get(pk=id)
    msg=None
    #form = cartBookForm(instance=book)
    cart = cartBooks(enterId=book.enterId,enterName=book.enterName,enterAuthorName=book.enterAuthorName,price=book.price)
    cart.save()
    msg = "book is taken"
    return HttpResponse(msg)
def returnBook(request, id):
    cart = cartBooks.objects.get(enterId=id)
    cart.delete()
    msg = "book is returned"
    return HttpResponse(msg)

def adminpage(request,id=0):
    msg=None
    bookinfo = Book.objects.all()
    if request.method == "POST":
        if id==0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            msg = 'Book is added successfully'
            return redirect('LibraryManagementSystem:adminpage')
        else:
            msg = 'book is not added'
            return redirect('LibraryManagementSystem:adminpage')
    else:
        if id==0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form=BookForm(instance=book)
    return render(request, 'admin.html', {'form': form, 'msg': msg, 'bookinfo': bookinfo})

class AllProducts(TemplateView):
    template_name = "products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Book.objects.all()
        return context


def AddToCart(request):
    return messages("Product is added to cart successfully")


def bookdelete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('LibraryManagementSystem:adminpage')


def bookupdate(request, id):
    bookinfo = Book.objects.all()
    book = Book.objects.get(pk=id)
    return render(request, "bookupdate.html",{'book': book,'bookinfo': bookinfo})

def dobookupdate(request, id):
    bookinfo = Book.objects.all()
    enterId = request.POST.get("enterId")
    enterName= request.POST.get("enterName")
    enterAuthorName= request.POST.get("enterAuthorName")
    price= request.POST.get("price")
    book = Book.objects.get(pk=id)
    book.enterId = enterId
    book.enterName = enterName
    book.enterAuthorName = enterAuthorName
    book.price = price
    book.save()
    return redirect('LibraryManagementSystem:adminpage')

class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        #kw = self.request.GET.get('keyword')
        results = Book.objects.filter(enterName__icontains=kw)
        context['results'] = results
        return context
'''
class AdminSignupView(generics.GenericAPIView):
    serializer_class = AdminSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "account created successfully"
        })
'''
class AdminSignupView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class ClientSignupView(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "account created successfully"
        })

@api_view(['POST'])
def registrationView(request):
    if request.method == 'POST':
        serializer = AdminSignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)