from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.domain.Transaction import Transaction
from api.serializers.TransactionSerializer import TransactionSerializer


from api.utils.ErrorMessages import ErrorMessages

class TransactionView(viewsets.ModelViewSet):  
    permission_classes = [IsAuthenticated] 
    
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
