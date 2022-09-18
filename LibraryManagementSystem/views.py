from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status 
import mysql.connector as sql

from LibraryManagementSystem.models import NewuserModel
from LibraryManagementSystem.serializers import NewuserModelSerializer
from rest_framework.decorators import api_view



def home(request): 
    return render(request, "base.html")

def addbooks(request):
    return render(request, "add_book.html")

def editbooks(request):
    return render(request, "edit_book.html")

def payments(request):
    return render(request, "payment_details.html")

def grid(request):
    return render(request, "grid.html")



     


# Create your views here.
def signaction(request):
    if request.method == "POST":
        usertype = request.POST.get('usertype')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('phonenumber')
        password = request.POST.get('password1')
        confirmpassword = request.POST.get('password2')

        data={'usertype':usetype,'username':username,'email':email,'phonenumber':phonenumber,
        'password':password1,'confirmpassword':password2}
        headers={'Content-Type':'application/json'}
        read=requests.POST('http://127.0.0.1:8000/signaction',json=data,headers=headers)       
        
        
        
        return render(request, "signup.html")
    else:
        return render(request, "signup.html")



def loginaction(request):
    global email,pwd1
    if request.method=="POST":
        m=sql.connect(host="mytestmysql",user="root",passwd="Rajiraghav*87",database='librarydb')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                pwd1=value
        
        c="select * from users where email='{}' and password1='{}'".format(email,pwd1)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"index.html")

    return render(request,'login.html')




@csrf_exempt 

def usersApi(self,request):
    if request.method=='GET':
        users=NewuserserModel.objects.all()
        users_serializer=NewuserserModeSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        users_serializer=NewuserModelSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.data,status=status.HTTP_400_BAD_RUQUEST)
             
    elif request.method=='PUT':
         users_data=JSONParser().parse(request)
         users=NewuserModel.objects.get(id=users_data['id'])
         users_serializer=NewuserModelSerializer(users,data=users_data)
         if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        users=NewuserModel.objects.get(id=id)
        users.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse("Failed to Delete",safe=False)
    
    
   

@csrf_exempt    

def adminsApi(request,id=0):
    if request.method=='GET':
        admins=AdminModel.objects.all()
        admins_serializer=AdminModelSerializer(admins,many=True)
        return JsonResponse(admins_serializer.data,safe=False)
    elif request.method=='POST':
        admins_data=JSONParser().parse(request)
        admins_serializer=AdminModelSerializer(data=admins_data)
        if admins_serializer.is_valid():
            admins_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
         admins_data=JSONParser().parse(request)
         admins=AdminModel.objects.get(id=admins_data['id'])
         admins_serializer=AdminModelSerializer(admins,data=admins_data)
         if admins_serializer.is_valid():
            admins_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
         return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        admins=AdminModel.objects.get(id=id)
        admins.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse("Failed to Delete",safe=False)








