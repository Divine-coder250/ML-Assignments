from django.db import models
from properties.models import Property

class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    lease_start = models.DateField()
    lease_end = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
