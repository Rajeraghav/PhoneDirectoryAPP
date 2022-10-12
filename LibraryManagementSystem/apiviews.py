from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import *
from django.db.models import Q
# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/admin/bookList/',
        'Detail View': '/admin/bookDetail/<str:pk>/',
        'Create': '/admin/addbook/',
        'Update': '/admin/updateBook/<str:pk>/',
        'Delete': '/admin/deleteBook/<str:pk>/',
        'user-list': '/admin/user-list/',
        'add User': '/admin/adduser/',
        'search' : 'search/<str:pk>',
        'payment-List': '/payment-list/',
        'payment': '/payment/',
        'lend': '/lend/',
        'return': '/return/<str:pk>/'

    }

    return Response(api_urls)


@api_view(['GET'])
def bookList(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bookDetail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def lendBook(request):
    serializer = CartBookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['DELETE'])
def returnBook(request, pk):
    book = cartBooks.objects.get(pk=pk)
    serializer = CartBookSerializer(book, many=False)
    book.delete()
    return Response(serializer.data)



@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def bookUpdate(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book, many=False)
    book.delete()
    return Response(serializer.data)

@api_view(['GET'])
def booksearch(request, pk):
    book = Book.objects.filter(Q(enterName__icontains=kw) | Q(enterAuthorName__icontains=kw))
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def payment(request):
    serializer = PaymentDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def paymentList(request):
    payment = PaymentDetails.objects.all()
    serializer = PaymentDetailsSerializer(payment, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user(request):
    serializer = AddUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def userList(request):
    user = User.objects.all()
    #user = addUser.objects.all()
    serializer = AddUserSerializer(user, many=True)
    return Response(serializer.data)
