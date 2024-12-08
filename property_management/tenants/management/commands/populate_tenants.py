from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from properties.models import Property
from tenants.models import Tenant

class Command(BaseCommand):
    help = 'Populates the Tenant table with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        properties = Property.objects.all()

        if not properties:
            self.stdout.write(self.style.ERROR("No properties found. Add properties first."))
            return

        self.stdout.write("Generating sample tenants...")

        for _ in range(10):
            lease_start = fake.date_this_year()
            lease_end = lease_start + timedelta(days=random.randint(180, 365))
            phone = fake.phone_number()[:15]

            tenant = Tenant.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=phone,
                property=random.choice(properties),
                lease_start=lease_start,
                lease_end=lease_end,
            )
            self.stdout.write(self.style.SUCCESS(f"Created tenant: {tenant}"))

        self.stdout.write(self.style.SUCCESS("Sample data generation completed."))
