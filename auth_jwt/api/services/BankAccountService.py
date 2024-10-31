from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError
from api.models.BankAccount import BankAccount
from api.serializers.BankAccountSerializer import BankAccountSerializer


class BankAccountService:
    
    @staticmethod
    def create(data):
        serializer = BankAccountSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)  
            return serializer.save()  
        except ValidationError as e:
            return {"errors": e.detail} 
       
    @staticmethod
    def list_paged(page=1, page_size=10):
        get_accounts = BankAccount.objects.all()
        paginator_instance = Paginator(get_accounts, page_size)

        try:
            get_accounts_paged = paginator_instance.page(page)  
        except EmptyPage:
            get_accounts_paged = []

        serializer = BankAccountSerializer(get_accounts_paged, many=True)
        
        return {
            'accounts': serializer.data,
            'total': get_accounts_paged.count, 
            'page': page,
            'page_size': page_size,
            'total_pages': get_accounts_paged.num_pages, 
        }

    @staticmethod
    def get(id):
        getUsuario = BankAccount.objects.filter(id=id).first()
        if getUsuario:
            serializer = BankAccountSerializer(getUsuario) 
            return serializer.data
        return None
    
