from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError
from api.models.Transaction import Transaction
from api.serializers.TransactionSerializer import TransactionSerializer


class TransactionService:
    
    @staticmethod
    def create(data):
        serializer = TransactionSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)  
            return serializer.save()  
        except ValidationError as e:
            return {"errors": e.detail} 
       
    @staticmethod
    def ListPaged(page=1, page_size=10):
        get_transactions = Transaction.objects.all()
        paginator_instance = Paginator(get_transactions, page_size)

        try:
            get_transactions_paged = paginator_instance.page(page)  
        except EmptyPage:
            get_transactions_paged = []

        serializer = TransactionSerializer(get_transactions_paged, many=True)
        
        return {
            'transactions': serializer.data,
            'total': get_transactions_paged.count, 
            'page': page,
            'page_size': page_size,
            'total_pages': get_transactions_paged.num_pages, 
        }

    @staticmethod
    def get(id):
        getUsuario = Transaction.objects.filter(id=id).first()
        if getUsuario:
            serializer = TransactionSerializer(getUsuario) 
            return serializer.data
        return None
    
