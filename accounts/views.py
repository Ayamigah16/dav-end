# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Account
# from .serializers import AccountSerializer

# class IsTeller(IsAuthenticated):
#     def has_permission(self, request, view):
#         return super().has_permission(request, view) and request.user.role == 'Teller'

# class AccountViewSet(viewsets.ModelViewSet):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

#     def get_permissions(self):
#         if self.action == 'list':
#             permission_classes = [IsAdminUser | IsTeller]
#         elif self.action == 'create':
#             permission_classes = [IsTeller]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]