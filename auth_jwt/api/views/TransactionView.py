from api.serializers.TransactionSerializer import TransactionSerializer
from api.services.TransactionService import TransactionService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 

from api.utils.ErrorMessages import ErrorMessages

class TransactionView(APIView):  
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        serializer = TransactionSerializer(data=request.data) 
        
        if serializer.is_valid():  
            created_bank_account = serializer.save() 
            return Response(TransactionSerializer(created_bank_account).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            bank_account = TransactionService.get(id)
            if bank_account:
                return Response(TransactionSerializer(data=bank_account).data, status=status.HTTP_200_OK)
            return Response(ErrorMessages.get_error('NOT_FOUND'), status=status.HTTP_404_NOT_FOUND)
        else:
            page = request.query_params.get('page', 1)
            page_size = request.query_params.get('page_size', 10)
            paged_result = TransactionService.list_paged(page, page_size)

            if not paged_result.object_list:
                return Response(ErrorMessages.get_error('PAGED_NOT_RESULT'), status=status.HTTP_404_NOT_FOUND)
            else:
                data = {
                    'total_count': paged_result.paginator.count,  
                    'number': paged_result.number, 
                    'total_pages': paged_result.paginator.num_pages, 
                    "data": TransactionSerializer(paged_result.object_list, many=True).data
                }
                return Response(data, status=status.HTTP_200_OK)