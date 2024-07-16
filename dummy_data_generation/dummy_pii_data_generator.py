from turtle import st
import pandas as pd
import random
from datetime import datetime, timedelta
from email_domains import email_domains
from phone_codes import country_codes
from faker import Faker
import re

# Create a Faker instance
fake = Faker()

def random_date(start_date, end_date):
    """
    Generate a random date between two dates.
    
    :param start_date: The start date in 'YYYY-MM-DD' format.
    :param end_date: The end date in 'YYYY-MM-DD' format.
    :return: A random date between start_date and end_date.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_phone_number_with_country_code(max_length:int = 13):
    phone_number = fake.phone_number()
    cleaned_number = re.sub(r'[^0-9+() -]', '', phone_number)
    cleaned_number = cleaned_number[:max_length]
    return cleaned_number


start_age = 18
end_age = 100

get_age = lambda x,y: random.randint(start_age, end_age)

Start_date = "1947-08-15"
end_date   = "2023-08-15"

df = pd.read_csv("dummy_data_generation/all-names.csv", delimiter=',', usecols=["sex","name"])

data_length = len(df.index)

df["age"] = [get_age(start_age, end_age) for x in range(data_length)]
df['date_of_birth'] = [random_date(Start_date, end_date) for x in range(data_length)]
df['email'] = [name.lower()+"@"+random.choice(email_domains) for name in df['name']]
df['phone'] = [generate_phone_number_with_country_code() for x in range(data_length)]


print(data_length)

random_date_generated = random_date(Start_date, end_date)
print(random_date_generated, "Random Date:", random_date_generated.strftime("%Y-%m-%d"))
print(get_age(start_age, end_age))


print(df.head())

print(df.tail())

df.to_csv("dummy_data_generation/sample_output_data.csv", index=False)