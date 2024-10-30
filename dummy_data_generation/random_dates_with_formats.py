import csv
import random
from datetime import datetime, timedelta

# List of supported date formats by PySpark
date_formats = [
    "yyyy-MM-dd",
    "yyyy/MM/dd",
    "yyyy.MM.dd",
    "MM/dd/yyyy",
    "dd MMM yyyy",
    "dd MMMM yyyy",
    "yyyy-mm-dd hh:mm:ss",
    "yyyy-mm-dd hh:mm:ss.SSS"
]

# Function to generate a random date string
def generate_random_date(format):
    # Generate a random date between today and 1 year ago
    random_date = datetime.now() - timedelta(days=random.randint(0, 365))
    return random_date.strftime(format.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d").replace("hh", "%H").replace("mm", "%M").replace("ss", "%S").replace("SSS", "%f"))

# Generate 100 rows of a column in a CSV file
with open('random_dates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["date"])  # header row
    format = random.choice(date_formats)
    for _ in range(100):
        writer.writerow([generate_random_date(format)])