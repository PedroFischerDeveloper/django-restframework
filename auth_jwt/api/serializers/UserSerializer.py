from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ['username', 'email', 'password'] 
        extra_kwargs = {
            'password': {'write_only': True} 
        }

    def create(self, validated_data):
        usuario = User(
            username=validated_data['username'],  
            email=validated_data['email'],
        )
        usuario.set_password(validated_data['password']) 
        usuario.save() 
        return usuario

    def __str__(self):
        return self.username