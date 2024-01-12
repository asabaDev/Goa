from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("The deposit amount must be positive.")
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("The withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValidationError("Insufficient funds.")
        self.balance -= amount
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Bank Account"
