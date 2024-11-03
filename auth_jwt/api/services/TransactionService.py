from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError
from api.models.Transaction import Transaction
from api.serializers.TransactionSerializer import TransactionSerializer


class TransactionService:
    
    @staticmethod
    def create(data):
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            return serializer.save()  
        return None  
       
    @staticmethod
    def list_paged(page=1, page_size=10):
        get_accounts = Transaction.objects.all()
        paginator_instance = Paginator(get_accounts, page_size)

        if paginator_instance.count == 0:
           return 0
        else: 
            get_accounts_paged = paginator_instance.page(page) 
            return get_accounts_paged

    @staticmethod
    def get(id):
        getUsuario = Transaction.objects.filter(id=id).first()
        if getUsuario:
            serializer = TransactionSerializer(getUsuario) 
            return serializer.data
        return None
    
