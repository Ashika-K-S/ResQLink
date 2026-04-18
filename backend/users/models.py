from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('volunteer', 'Volunteer'),
        ('authority', 'Authority'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='citizen'
    )

    phone = models.CharField(max_length=15, blank=True)

    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return f"{self.username} ({self.role})"