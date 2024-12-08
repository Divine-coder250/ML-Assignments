from django.core.management.base import BaseCommand
from faker import Faker
import random
from tenants.models import Tenant
from maintenance.models import Maintenance

class Command(BaseCommand):
    help = 'Populates the Maintenance table with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        tenants = Tenant.objects.all()

        if not tenants.exists():
            self.stdout.write(self.style.ERROR("No tenants found. Add tenants before generating maintenance records."))
            return

        self.stdout.write("Generating sample maintenance records...")

        for _ in range(15):  # Generate 15 maintenance records
            tenant = random.choice(tenants)
            issue = fake.sentence(nb_words=5)  # A short title for the issue
            description = fake.paragraph(nb_sentences=3)  # Detailed description of the issue
            status = random.choice(['Pending', 'In Progress', 'Resolved'])  # Random status

            # Create maintenance record
            maintenance = Maintenance.objects.create(
                tenant=tenant,
                issue=issue,
                description=description,
                status=status,
            )
            self.stdout.write(self.style.SUCCESS(f"Created maintenance record: {maintenance}"))

        self.stdout.write(self.style.SUCCESS("Sample data generation completed."))
