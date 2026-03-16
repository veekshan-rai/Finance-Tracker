from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = [
    ('Income', 'Income'),
    ('Expense', 'Expense')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=265)
    amount = models.DecimalField( max_digits=10 , decimal_places=2)
    transaction_type = models.CharField(max_length=10, 
                                    choices=TRANSACTION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    target_amount = models.DecimalField( max_digits=10, decimal_places=2)
    deadline = models.DateField()
    class Meta:
        verbose_name_plural = "Goals" # adding this if it is not there in admin panel it shows like Goalss like thet so we can create this
        

    def __str__(self):
        return self.user

