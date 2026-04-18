from django.db import models

class Resource(models.Model):
    RESOURCE_TYPE = (
        ('ambulance', 'Ambulance'),
        ('blood', 'Blood'),
        ('fire_truck', 'Fire Truck'),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPE)
    available = models.BooleanField(default=True)