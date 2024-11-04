from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError
from api.domain.BankAccount import BankAccount
from api.serializers.BankAccountSerializer import BankAccountSerializer


class BankAccountService:
    
    @staticmethod
    def create(data):
        serializer = BankAccountSerializer(data=data)
        if serializer.is_valid():
            return serializer.save()  
        return None  
       
    @staticmethod
    def list_paged(page=1, page_size=10):
        get_accounts = BankAccount.objects.all()
        paginator_instance = Paginator(get_accounts, page_size)

        if paginator_instance.count == 0:
           return 0
        else: 
            get_accounts_paged = paginator_instance.page(page) 
            return get_accounts_paged

    @staticmethod
    def get(id):
        getUsuario = BankAccount.objects.filter(id=id).first()
        if getUsuario:
            serializer = BankAccountSerializer(getUsuario) 
            return serializer.data
        return None
    
