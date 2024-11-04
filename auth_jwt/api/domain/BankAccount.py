from django.db import models
from django.contrib.auth.models import User


class BankAccount(models.Model):
    ACCOUNT_TYPES = [
        ('C', 'CHEKING'),
        ('S', 'SAVINGS'),
    ]

    STATUS_CHOICE = [
        ('A', 'ACTIVE'),
        ('C', 'CLOSED'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_accounts")
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)

    def __str__(self):
        return self.account_number
