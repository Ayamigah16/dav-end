from rest_framework import serializers
from .models import Account, Customer

class CustomerSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_email', 'contact_number', 'address']

class AccountSerializer(serializers.ModelSerializer):
    customer_email = serializers.EmailField(source="customer.user.email", read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'customer', 'customer_email', 'account_type', 'balance', 'created_at']
        read_only_fields = ['balance', 'created_at']