from api.serializers.GetUserSerializer import GetUserSerializer
from api.serializers.UserSerializer import UserSerializer
from api.serializers.ListUserPagedSerializer import ListUserPagedSerializer
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserService:
    
    @staticmethod
    def criar_usuario(data):
        serializer = UserSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)  
            return serializer.save()  
        except ValidationError as e:
            return {"errors": e.detail} 

    @staticmethod
    def valida_usuario_existente(email):
        return User.objects.filter(email=email).first()
       
    @staticmethod
    def get_paginated_usuarios(page=1, page_size=10):
        usuarios = User.objects.all()
        paginado = Paginator(usuarios, page_size)

        try:
            usuarios_page = paginado.page(page)  
        except EmptyPage:
            usuarios_page = []

        serializer = ListUserPagedSerializer(usuarios_page, many=True)
        
        return {
            'usuarios': serializer.data,
            'total': paginado.count, 
            'page': page,
            'page_size': page_size,
            'total_pages': paginado.num_pages, 
        }

    @staticmethod
    def busca_usuario_por_id(id):
        getUsuario = User.objects.filter(id=id).first()
        if getUsuario:
            serializer = GetUserSerializer(getUsuario) 
            return serializer.data
        return None
    
