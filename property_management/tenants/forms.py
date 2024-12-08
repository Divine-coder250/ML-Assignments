from django import forms
from .models import Tenant  # Assuming you have a Tenant model in tenants/models.py

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'  # Use '__all__' to include all model fields or specify fields like ['first_name', 'last_name']
