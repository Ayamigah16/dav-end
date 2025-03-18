from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction, Account
from .serializers import TransactionSerializer
from decimal import Decimal

class IsTeller(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == 'Teller'

class IsCustomer(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == 'Customer'

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        account = Account.objects.get(id=request.data['account_id'])
        amount = Decimal(request.data['amount'])
        account.balance += amount
        account.save()
        return Response({'message': 'Deposit successful'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def withdraw(self, request):
        account = Account.objects.get(id=request.data['account_id'])
        amount = Decimal(request.data['amount'])
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            return Response({'message': 'Withdrawal successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def transfer(self, request):
        from_account = Account.objects.get(id=request.data['from_account_id'])
        to_account = Account.objects.get(id=request.data['to_account_id'])
        amount = Decimal(request.data['amount'])
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            return Response({'message': 'Transfer successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)