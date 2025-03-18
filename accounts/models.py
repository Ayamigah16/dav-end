from django.db import models
from users.models import User

class Customer(models.Model):
    """A Customer is a User with extra details like contact & address."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.email


class Account(models.Model):
    """An Account belongs to a Customer and has a type & balance."""
    ACCOUNT_TYPES = (
        ('Savings', 'Savings'),
        ('Current', 'Current')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.user.email} - {self.account_type} (${self.balance})"
