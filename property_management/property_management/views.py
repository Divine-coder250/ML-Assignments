from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from tenants.models import Tenant
from datetime import date, timedelta
from collections import Counter

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to the homepage or a desired page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def landing_page(request):
    return render(request, 'landing.html')

@login_required
def homepage(request):
    tenants = Tenant.objects.all()
    date_counts = Counter()

    # Track dates for each tenant's lease period
    for tenant in tenants:
        start_date = tenant.lease_start
        end_date = tenant.lease_end or date.today()  # Use today if lease_end is None.
        current_date = start_date

        # Loop through each day in the tenant's lease period
        while current_date <= end_date:
            date_counts[current_date] += 1
            current_date += timedelta(days=1)  # Increment day by day.

    sorted_counts = sorted(date_counts.items())  # Sort by date.
    labels = [item[0].strftime('%Y-%m-%d') for item in sorted_counts]
    data = [item[1] for item in sorted_counts]

    # Print data for debugging
    # print("Labels:", labels)
    # print("Data:", data)

    return render(request, 'homepage.html', {'labels': labels, 'data': data})