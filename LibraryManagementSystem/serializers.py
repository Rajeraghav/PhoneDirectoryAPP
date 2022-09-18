from rest_framework import serializers
from LibraryManagementSystem.models import Newuser

class NewuserModelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = NewuserModel
        fields ="__all__"
       

