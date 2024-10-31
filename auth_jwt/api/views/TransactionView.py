from api.serializers.BankAccountSerializer import BankAccountSerializer
from api.services.TransactionService import TransactionService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 

class TransactionView(APIView):  
    permission_classes = [IsAuthenticated] 

    def post(self, request):   
        created_bank_account = TransactionService.create(data=request.data)
        if created_bank_account:
            return Response(BankAccountSerializer(created_bank_account).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        usuario_existe = TransactionService.get(id)
        if usuario_existe:
            return Response(usuario_existe, status=status.HTTP_200_OK)
        return Response({'error': 'Usuário não localizado'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        page = request.query_params.get('page', 1) 
        page_size = request.query_params.get('page_size', 10) 
        paginated_usuarios = TransactionService.list_paged(page, page_size)
        return Response(paginated_usuarios, status=status.HTTP_200_OK)