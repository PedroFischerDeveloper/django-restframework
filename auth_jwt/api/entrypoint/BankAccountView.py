from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from api.domain.BankAccount import BankAccount
from api.serializers.BankAccountSerializer import BankAccountSerializer


from api.service_layer import BankAccountService
from api.utils.ErrorMessages import ErrorMessages

class BankAccountView(APIView):  
    permission_classes = [IsAuthenticated] 

    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

    def list(self, request, pk=None, *args, **kwargs):
        queryset = BankAccountService.get_all_bank_account()
            
             

            
            
   