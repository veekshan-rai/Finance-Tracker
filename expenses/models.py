from django.db import models
from django.contrib.auth.models import User
TRANSACTION_TYPES = [
    ('Income', 'Income'),
    ('Expense', 'Expense')
]

user = models.ForeignKey(User, on_delete=models.CASCADE)
class Transaction(models.Model):
    title = models.CharField(max_length=265)
    amount = models.DecimalField( max_digits=5, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices= TRANSACTION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=255)

