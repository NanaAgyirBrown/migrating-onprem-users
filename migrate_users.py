import csv
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Data to generate
roles = ["DevEngineer", "DBA", "Trainee", "CloudAdmin", "LinuxAdmin"]

# Generate random passwords
def generate_password(length=10):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$"
    return ''.join(random.choice(characters) for _ in range(length))

# Generate employee data with realistic names
def generate_employee_data(num_employees):
    employees = []
    for _ in range(num_employees):
        name = fake.name()
        email = f"{name.replace(' ', '.').lower()}@xyz-company.com"
        role = random.choice(roles)
        password = generate_password()
        employees.append({"name": name, "email": email, "role": role, "password": password})
    return employees

# Generate CSV
file_path = "employees_list.csv"
employees = generate_employee_data(100)

with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email", "role", "password"])
    writer.writeheader()
    writer.writerows(employees)

print(f"File created: {file_path}")
