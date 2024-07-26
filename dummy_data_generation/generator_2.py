import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_dummy_ssn():
    """Generate a random dummy Social Security Number (SSN)."""
    area_number = random.randint(100, 999)  # First three digits (AAA)
    group_number = random.randint(1, 99)     # Next two digits (GG)
    serial_number = random.randint(1, 9999)  # Last four digits (SSSS)
    return f"{area_number:03}-{group_number:02}-{serial_number:04}"

def generate_dummy_ein():
    """Generate a random dummy Employer Identification Number (EIN)."""
    prefix = random.randint(10, 99)  # First two digits (XX)
    suffix = random.randint(1000000, 9999999)  # Last seven digits (XXXXXXX)
    return f"{prefix:02}-{suffix:07}"

def generate_dummy_itin():
    """Generate a random dummy Individual Taxpayer Identification Number (ITIN)."""
    area_number = random.randint(900, 999)  # First three digits (9XX)
    group_number = random.choice([7, 8])     # Next digit (7X or 8X)
    serial_number = random.randint(1000, 9999)  # Last four digits (XXXX)
    return f"{area_number}-{group_number}{random.randint(0, 9)}-{serial_number:04}"

# Generate dummy TINs
# dummy_ssn = generate_dummy_ssn()
# dummy_ein = generate_dummy_ein()
# dummy_itin = generate_dummy_itin()

# print("Dummy SSN:", dummy_ssn)
# print("Dummy EIN:", dummy_ein)
# print("Dummy ITIN:", dummy_itin)


print(fake.ssn(), fake.ein(), fake.itin())


df = pd.read_csv("dummy_data_generation/sample_output_data_1.csv")


data_length = len(df.index)

SSN = []
EIN = []
ITIN = []
ADDRESS = []

for i in range(data_length):
    SSN.append(fake.ssn())
    EIN.append(fake.ein())
    ITIN.append(fake.itin())
    ADDRESS.append(fake.address())

df['Address'] = ADDRESS
df['SSN'] = SSN
df['Employer_ID_No'] = EIN
df['TAXID'] = ITIN






print(df.head())
print(df.tail())

df.to_csv("dummy_data_generation/sample_output_data_2.csv", index=False)