import random
import pandas as pd
from faker import Faker
import string

def generate_dummy_us_license(state_code):
    """Generate a random dummy US driving license number."""
    numeric_part = ''.join(random.choices(string.digits, k=7))  # 7 digits
    return f"{state_code}{numeric_part}"

def generate_dummy_uk_license(code):
    """Generate a random dummy UK driving license number."""
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))  # 2 letters
    digits = ''.join(random.choices(string.digits, k=6))            # 6 digits
    check_letter = random.choice(string.ascii_uppercase)            # 1 letter
    return f"{letters}{digits}{check_letter}"

def generate_dummy_germany_license(code):
    """Generate a random dummy German driving license number."""
    state_initial = random.choice(string.ascii_uppercase)  # 1 letter
    numeric_part = ''.join(random.choices(string.digits, k=7))  # 7 digits
    return f"{state_initial}{numeric_part}"

def generate_dummy_france_license(code):
    """Generate a random dummy French driving license number."""
    return ''.join(random.choices(string.digits, k=13))  # 13 digits

driving_license = [generate_dummy_us_license,generate_dummy_uk_license,generate_dummy_germany_license,generate_dummy_france_license]

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


# print(fake.ssn(), fake.ein(), fake.itin())


df = pd.read_csv("dummy_data_generation/sample_output_data_1.csv")


data_length = len(df.index)

SSN = []
EIN = []
ITIN = []
STREET_ADDRESS = []
STATE = []
COUNTRY = []
BirthPlace = []
PassportInfo = []
CITY = []
DrivingLicense = []




for i in range(data_length):
    SSN.append(fake.ssn())
    EIN.append(fake.ein())
    ITIN.append(fake.itin())
    STREET_ADDRESS.append(fake.street_address())
    STATE.append(fake.state())
    COUNTRY.append(fake.country())
    BirthPlace.append(fake.city())
    PassportInfo.append(fake.passport_full())
    CITY.append(fake.city())
    DrivingLicense.append(random.choice(driving_license)(fake.state_abbr()))




df['BirthPlace']     = BirthPlace
df['Streed_Address'] = STREET_ADDRESS
df['State']          = STATE
df['Country']        = COUNTRY
df['SSN']            = SSN
df['Employer_ID_No'] = EIN
df['TAXID']          = ITIN
df['PassportInfo']   = PassportInfo
df['DriverLicense']  = DrivingLicense





print(df.head())
print(df.tail())

df.to_csv("dummy_data_generation/sample_output_data_2.csv", index=False)