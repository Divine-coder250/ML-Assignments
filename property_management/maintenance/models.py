from django.db import models
from tenants.models import Tenant

class Maintenance(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    issue = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue} - {self.tenant}"
