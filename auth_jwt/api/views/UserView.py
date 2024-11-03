from api.serializers.UserSerializer import UserSerializer
from api.services.UserService import UserService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.utils.ErrorMessages import ErrorMessages


class UserView(APIView):  
    
    def post(self, request):
        get_user = UserService.valida_usuario_existente(request.data.get('email'))
        if get_user:
             return Response(ErrorMessages.get_error('USER_EXISTS'), status=status.HTTP_400_BAD_REQUEST)
        
        getUsuario = UserService.criar_usuario(data=request.data)
        if getUsuario:
            return Response(UserSerializer(getUsuario).data, status=status.HTTP_201_CREATED)
        return Response(ErrorMessages.get_error("INVALID_DATE"), status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        if id:
            get_user = UserService.busca_usuario_por_id(id)
            if get_user:
                return Response(UserSerializer(get_user).data, status=status.HTTP_200_OK)
            return Response(ErrorMessages.get_error('NOT_FOUND'), status=status.HTTP_404_NOT_FOUND)
        else:
            page = request.query_params.get('page', 1)
            page_size = request.query_params.get('page_size', 10)
            paged_result = UserService.get_paginated_usuarios(page, page_size)
            return Response(UserSerializer(paged_result).data, status=status.HTTP_200_OK)
