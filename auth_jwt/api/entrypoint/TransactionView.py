# Importando bibliotecas de terceiros
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.serializers.TransactionSerializer import TransactionSerializer
from api.service_layer.TransactionService import TransactionService



class TransactionView(viewsets.ModelViewSet):  
    serializer_class = TransactionSerializer
    queryset = TransactionService.get_all_transaction()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

    def list(self, request, *args, **kwargs):
        queryset = TransactionService.get_all_transaction()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        user = TransactionService.get_transaction_by_id(pk)
        if user is not None:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        user = TransactionService.create_transaction(request.data)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        user = TransactionService.update_transaction(pk, request.data)
        if user is not None:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None, *args, **kwargs):
        success = TransactionService.delete_transaction(pk)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
