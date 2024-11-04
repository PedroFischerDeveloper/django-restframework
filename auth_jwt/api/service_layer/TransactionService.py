# Importando bibliotecas de terceiros
from django.core.exceptions import ObjectDoesNotExist

# Importando módulos locais
from api.domain.Transaction import Transaction

class TransactionService:
    @staticmethod
    def get_all_transaction():
        return Transaction.objects.all()
        

    @staticmethod
    def get_transaction_by_id(user_id):
        try:
            return Transaction.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None
        
    @staticmethod
    def create_transaction(data):
        transaction = Transaction(**data)
        transaction.save()
        return transaction

    @staticmethod
    def update_transaction(transaction_id, data):
        try:
            transaction = TransactionService.get_transaction_by_id(transaction_id)
            if transaction is not None:
                for attr, value in data.items():
                    setattr(transaction, attr, value)
                transaction.save()
                return transaction
            return None
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_transaction(transaction_id):
        try:
            transaction = TransactionService.get_transaction_by_id(transaction_id)
            if transaction is not None:
                transaction.delete()
                return True
            return False
        except ObjectDoesNotExist:
            return False
    
