from django.contrib import admin
from api.domain.BankAccount import BankAccount
from api.domain.Transaction import Transaction

admin.site.register(BankAccount)
admin.site.register(Transaction)
