import psycopg2
import csv

# Database connection
conn = psycopg2.connect(
    dbname="properties_db",
    user="postgres",
    password="!Mamadivine12345",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Open the CSV file
with open('dataset2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO tenants (name, email, property_id) VALUES (%s, %s, %s)",
            row
        )

# Commit and close
conn.commit()
cursor.close()
conn.close()
