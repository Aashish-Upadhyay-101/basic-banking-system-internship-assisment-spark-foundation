from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Transfer(models.Model):
    user = models.ForeignKey(User, related_name="transfer", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"to {self.user.username}-${self.amount}"


        