from django.shortcuts import render, redirect, get_object_or_404
from .models import Tenant
from .forms import TenantForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/tenant_list.html', {'tenants': tenants})

def tenant_detail(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    return render(request, 'tenants/tenant_detail.html', {'tenant': tenant})
def tenant_create(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')  # Redirect to the tenant list page
    else:
        form = TenantForm()
    return render(request, 'tenants/tenant_form.html', {'form': form})
def tenant_update(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == "POST":
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')  # Redirect to the tenant list page
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/tenant_form.html', {'form': form})
def tenant_delete(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == "POST":
        tenant.delete()
        return HttpResponseRedirect(reverse('tenant_list'))  # Redirect to tenant list page
    return render(request, 'tenants/tenant_confirm_delete.html', {'tenant': tenant})
def tenant_update(request, id):  # Change 'pk' to 'id'
    tenant = get_object_or_404(Tenant, id=id)  # Update to 'id'
    if request.method == "POST":
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')  # Redirect to the tenant list or another relevant page
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/tenant_form.html', {'form': form, 'tenant': tenant})
def tenant_delete(request, id):  # Accept 'id' as an argument
    tenant = get_object_or_404(Tenant, id=id)  # Use 'id' to fetch the tenant
    tenant.delete()
    return redirect('tenant_list')  # Redirect to tenant list or another relevant page
def tenant_delete(request, id):  # Or use 'pk' if consistent with URLs
    tenant = get_object_or_404(Tenant, id=id)
    
    if request.method == "POST":
        tenant.delete()
        return redirect('tenant_list')  # Redirect to the tenant list page after deletion

    return render(request, 'tenants/tenant_delete.html', {'tenant': tenant})
