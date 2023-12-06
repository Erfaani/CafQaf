from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_types = [
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('normal', 'Normal User'),
    ]
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    type = models.CharField(max_length=10, choices=user_types, default='normal')

    def __str__(self):
        return self.username
    
