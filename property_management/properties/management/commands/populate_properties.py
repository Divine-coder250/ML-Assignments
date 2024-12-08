from django.core.management.base import BaseCommand
from faker import Faker
from properties.models import Property

class Command(BaseCommand):
    help = 'Populates the Property table with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("Generating sample properties...")

        for _ in range(10):  # Generate 10 sample properties
            name = fake.company()
            address = fake.address()
            owner = fake.name()
            price = round(fake.random_number(digits=5, fix_len=True) / 100, 2)  # Random price between 0 and 9999.99
            description = fake.text(max_nb_chars=200)  # Random description

            # Create property record
            property = Property.objects.create(
                name=name,
                address=address,
                owner=owner,
                price=price,
                description=description,
            )
            self.stdout.write(self.style.SUCCESS(f"Created property: {property}"))

        self.stdout.write(self.style.SUCCESS("Sample data generation completed."))
