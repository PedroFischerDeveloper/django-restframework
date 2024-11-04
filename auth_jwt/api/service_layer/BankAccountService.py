# Importando bibliotecas de terceiros
from django.core.exceptions import ObjectDoesNotExist

# Importando módulos locais
from api.domain.BankAccount import BankAccount


class BankAccountService:
    @staticmethod
    def get_all_bank_account():
        return BankAccount.objects.all()
        

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return BankAccount.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None
        
    @staticmethod
    def create_user(data):
        user = BankAccount(**data)
        user.save()
        return user

    @staticmethod
    def update_user(user_id, data):
        try:
            bankAccount = BankAccountService.get_user_by_id(user_id)
            if bankAccount is not None:
                for attr, value in data.items():
                    setattr(bankAccount, attr, value)
                bankAccount.save()
                return bankAccount
            return None
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            bankAccount = BankAccountService.get_user_by_id(user_id)
            if bankAccount is not None:
                bankAccount.delete()
                return True
            return False
        except ObjectDoesNotExist:
            return False
    
