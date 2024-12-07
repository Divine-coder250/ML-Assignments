import csv
import random  # Import for generating random values
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the num ber of records to generate
num_records = 500000

# Define the output file name
output_file = "dataset1.csv"
# Generate dataset
data = [
    {
       "Name": fake.name(),
        "Address": fake.country(),
        "Price": fake.random_int(min=2, max=120987777)
    }
    for _ in range(num_records)
]

# Save to CSV file
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Address", "Price"])
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset with {num_records} records saved to {output_file}.")