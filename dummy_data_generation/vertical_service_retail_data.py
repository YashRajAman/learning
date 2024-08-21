import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating dummy data
fake = Faker()

# Define the number of rows
num_rows = 100

# Create lists for the dataset
data = {
    "Customer ID": [fake.uuid4() for _ in range(num_rows)],
    "Name": [fake.name() for _ in range(num_rows)],
    "Email": [fake.email() for _ in range(num_rows)],
    "Phone Number": [fake.phone_number() for _ in range(num_rows)],
    "Age": [random.randint(18, 70) for _ in range(num_rows)],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(num_rows)],
    "Address": [fake.address().replace("\n", ", ") for _ in range(num_rows)],
    "City": [fake.city() for _ in range(num_rows)],
    "State": [fake.state() for _ in range(num_rows)],
    "Zip Code": [fake.zipcode() for _ in range(num_rows)],
    "Product ID": [fake.uuid4() for _ in range(num_rows)],
    "Product Name": [fake.word().capitalize() + " " + fake.word().capitalize() for _ in range(num_rows)],
    "Category": [random.choice(["Electronics", "Clothing", "Groceries", "Home", "Beauty"]) for _ in range(num_rows)],
    "Price": [round(random.uniform(5.0, 500.0), 2) for _ in range(num_rows)],
    "Quantity Purchased": [random.randint(1, 10) for _ in range(num_rows)],
    "Transaction Date": [fake.date_this_year() for _ in range(num_rows)],
    "Payment Method": [random.choice(["Credit Card", "PayPal", "Cash"]) for _ in range(num_rows)],
    "Total Amount": [round(random.uniform(10.0, 5000.0), 2) for _ in range(num_rows)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("retail_data.csv", index=False)

print("CSV file 'retail_data.csv' generated with 100 rows of dummy retail data.")