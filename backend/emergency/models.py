from django.db import models
from users.models import User

class Emergency(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='emergencies'
    )

    latitude = models.FloatField()
    longitude = models.FloatField()

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    assigned_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_emergencies'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Emergency {self.id} - {self.status}"