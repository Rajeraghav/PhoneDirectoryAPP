from rest_framework import serializers
from LibraryManagementSystem.models import Newuser

class NewuserModelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Newuser
        fields ="__all__"
        extra_kwargs = {'id': {'required': False}}

