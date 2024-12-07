import csv
import random  # Import for generating random values
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the num ber of records to generate
num_records = 10000

# Define the output file name
output_file = "dataset2.csv"

# Set to track unique emails
unique_emails = set()

# Function to generate a unique email
def generate_unique_email():
    email = fake.email()
    while email in unique_emails:
        email = fake.email()  # Regenerate if the email is already in the set
    unique_emails.add(email)
    return email

# Generate dataset
data = [
    {
        "Name": fake.name(),
        "Email": generate_unique_email(),
        "Property_id": fake.random_int(min=2, max=500000)
    }
    for _ in range(num_records)
]

# Save to CSV file
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Property_id"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset with {num_records} records saved to {output_file}.")