from rest_framework import serializers
from api.models.BankAccount import BankAccount

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        
    def validate(self, data):
        if 'user' not in data:
            raise serializers.ValidationError({"user": "This field is required."})
        if 'account_number' not in data:
            raise serializers.ValidationError({"account_number": "This field is required."})

        return data