from django.contrib import admin
from api.models.BankAccount import BankAccount
from api.models.Transaction import Transaction

admin.site.register(BankAccount)
admin.site.register(Transaction)
