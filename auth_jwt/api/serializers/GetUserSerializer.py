from rest_framework import serializers
from django.contrib.auth.models import User

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','username', 'email']  

        
        