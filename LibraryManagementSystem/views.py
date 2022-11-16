from django.contrib.auth.decorators import login_required
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
from .forms import SignUpForm, BookForm
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
    ms=None
    
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
        return render(request,'addUser.html', {'form': form})
      


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('LibraryManagementSystem:login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    msg = None
    if request.method == 'POST':
        email = request.POST.get("email")
        u = User.objects.get(email=email)
        username=u.username
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        #print(user)
        if user is not None and user.adminORuser == 'admin':
            login(request, user)
            return redirect('LibraryManagementSystem:adminpage')
        elif user is not None and user.adminORuser == 'user':
            login(request, user)
            return redirect('LibraryManagementSystem:customer')
        else:
            msg = 'invalid credentials'
    return render(request, 'login.html', {'msg': msg})


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
            enterId = request.POST.get("getBook")
            day = int(request.POST.get("enterDays"))
            form.save()
            book = Book.objects.get(enterId=enterId)
            price = int(book.price)
            msg = "Cost of the book is " + str(price*day)
            #return HttpResponse(msg)
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
    cart = cartBooks(enterId=book.enterId,enterName=book.enterName,enterAuthorName=book.enterAuthorName,
    price=book.price)
    cart.save()
    return render(request,'getBook.html')

def returnBook(request, id):
    cart = cartBooks.objects.get(enterId=id)
    cart.delete()
    return render(request,'returnBook.html')

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

'''
class AllProducts(TemplateView):
    template_name = "products.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Book.objects.all()
        return context
'''
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
        results = Book.objects.filter(Q(enterName__icontains=kw) | Q(enterAuthorName__icontains=kw))
        context['results'] = results
        return context


def logout_view(request):
    logout(request)
    return redirect('LibraryManagementSystem:login_view')