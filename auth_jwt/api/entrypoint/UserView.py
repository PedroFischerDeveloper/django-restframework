# Importando bibliotecas de terceiros
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response

# Importando módulos locais
from api.serializers.UserSerializer import UserSerializer
from api.service_layer.UserService import UserService


# Viewset base, fornece as operações básicas de leitura, cadastro, consulta, atualizações e deleções
class UserViewSet(viewsets.ModelViewSet):  
    serializer_class = UserSerializer
    queryset = UserService.get_all_users()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

    def list(self, request, *args, **kwargs):
        queryset = UserService.get_all_users()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        user = UserService.get_user_by_id(pk)
        if user is not None:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        user = UserService.create_user(request.data)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        user = UserService.update_user(pk, request.data)
        if user is not None:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        success = UserService.delete_user(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
