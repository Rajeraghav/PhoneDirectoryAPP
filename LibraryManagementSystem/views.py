from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from .forms import SignUpForm, LoginForm, BookForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from .serializer import *
from django.contrib import messages
from django.db.models import Q
from django.contrib import auth

# Create your views here.


def index(request):
    return render(request, 'index.html')


def addUser(request):
    ms = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            ms = 'user created'
            return redirect('LibraryManagementSystem:adminpage')
        else:

            ms = 'form is not valid'
    else:
        form = SignUpForm()
        return render(request, 'addUser.html', {'form': form, 'ms': ms})

'''
def register(request):
    msg = None
    if request.method == 'POST':
        adminORuser = request.POST.get("adminORuser")
        email = request.POST.get("email")
        username = request.POST.get("username")
        mobileNumber = request.POST.get("mobileNumber")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = User(adminORuser=adminORuser,email=email,
                    username=username,mobileNumber=mobileNumber,
                    password1=password1,password2=password2)
        user.save()
        msg = 'user created'
        return redirect('account:login-view')
    else:
        msg = 'form is not valid'
        return render(request, 'register.html', {'msg': msg})
    return render(request, 'register.html', {'msg': msg})
'''

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login-view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        who = user.adminORuser
        #print(user + who)
        if user is not None and who == 'admin':
            login(request, user)
            return redirect('account:adminpage')
        elif user is not None and who == 'user':
            login(request, user)
            return redirect('account:customer')
        if user is not None:
            return HttpResponse('loin')
        else:
            msg = 'invalid credentials'

    return render(request, 'login.html', { 'msg': msg})


'''
            elif user is not None and user.adminORuser:
                login(request, user)
                return redirect('account:customer')
'''


def customer(request, id=0):
    msg = None
    form = PaymentDetailsForm()
    bookinfo = Book.objects.all()
    if request.method == "POST":
        if id == 0:
            form = PaymentDetailsForm(request.POST)
        else:
            payment = PaymentDetailsForm.objects.get(pk=id)
            form = PaymentDetailsForm(request.POST, instance=payment)
        if form.is_valid():
            enterId = request.POST.get("getBook")
            day = int(request.POST.get("enterDays"))
            form.save()
            book = Book.objects.get(enterId=enterId)
            price = int(book.price)
            msg = "Cost of the book is " + str(price * day)
            return HttpResponse(msg)
        else:
            msg = 'Payment is not Done'
            return redirect('account:customer')
    else:
        if id == 0:
            form = PaymentDetailsForm()
        else:
            book = PaymentDetails.objects.get(pk=id)
            form = PaymentDetailsForm(request.POST, instance=book)
    return render(request, 'customer.html', {'form': form, 'msg': msg, 'bookinfo': bookinfo})


def getBook(request, id):
    book = Book.objects.get(pk=id)
    msg = None
    # form = cartBookForm(instance=book)
    cart = cartBooks(enterId=book.enterId, enterName=book.enterName, enterAuthorName=book.enterAuthorName,
                     price=book.price)
    cart.save()
    msg = "book is taken"
    return HttpResponse(msg)


def returnBook(request, id):
    cart = cartBooks.objects.get(enterId=id)
    cart.delete()
    msg = "book is returned"
    return HttpResponse(msg)


def adminpage(request, id=0):
    msg = None
    bookinfo = Book.objects.all()
    if request.method == "POST":
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            msg = 'Book is added successfully'
            return redirect('account:adminpage')
        else:
            msg = 'book is not added'
            return redirect('account:adminpage')
    else:
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
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
    return redirect('account:adminpage')


def bookupdate(request, id):
    bookinfo = Book.objects.all()
    book = Book.objects.get(pk=id)
    return render(request, "bookupdate.html", {'book': book, 'bookinfo': bookinfo})


def dobookupdate(request, id):
    bookinfo = Book.objects.all()
    enterId = request.POST.get("enterId")
    enterName = request.POST.get("enterName")
    enterAuthorName = request.POST.get("enterAuthorName")
    price = request.POST.get("price")
    book = Book.objects.get(pk=id)
    book.enterId = enterId
    book.enterName = enterName
    book.enterAuthorName = enterAuthorName
    book.price = price
    book.save()
    return redirect('account:adminpage')


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        # kw = self.request.GET.get('keyword')
        results = Book.objects.filter(Q(enterName__icontains=kw) | Q(enterAuthorName__icontains=kw))
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
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
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


def logout_view(request):
    logout(request)
    return redirect('account:login-view')
