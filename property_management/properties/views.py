from django.shortcuts import render, redirect
from .models import Property

# List all properties
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

# Create new property
def property_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        owner = request.POST['owner']
        price = request.POST['price']
        description = request.POST['description']
        Property.objects.create(name=name, address=address, owner=owner, price=price, description=description)
        return redirect('property_list')
    return render(request, 'properties/property_create.html')

# Update existing property
def property_update(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        property.name = request.POST['name']
        property.address = request.POST['address']
        property.owner = request.POST['owner']
        property.price = request.POST['price']
        property.description = request.POST['description']
        property.save()
        return redirect('property_list')
    return render(request, 'properties/property_update.html', {'property': property})

# Delete a property
def property_delete(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'properties/property_delete.html', {'property': property})
