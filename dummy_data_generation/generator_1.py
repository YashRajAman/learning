import random
import pandas as pd
import random
from bank_acc_generator import generate_bank_account_number

df = pd.read_csv("dummy_data_generation/sample_output_data.csv")

data_length = len(df.index)

def generate_debit_card_number(bin):
    """
    This function generates a random 16-digit debit card number.
    The first 6 digits are the Bank Identification Number (BIN), also known as the Issuer Identification Number (IIN).
    The next 9 digits are random.
    The last digit is a checksum.
    """
    # Generate the first 15 digits
    first_15_digits = bin + ''.join(random.choice('0123456789') for i in range(10))

    # Calculate the checksum
    checksum = 0
    for i in range(15):
        digit = int(first_15_digits[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    checksum = (10 - (checksum % 10)) % 10

    # Return the complete 16-digit debit card number
    return first_15_digits + str(checksum)


def generate_random_bin(x):
    """
    This function generates a random 6-digit Bank Identification Number (BIN) for x times.
    """
    for _ in range(x):
        bin = ''.join(random.choice('0123456789') for i in range(6))
        yield bin
        
def generate_card_exp_date():
    """
    Generate card expiry date in MM/yy format. eg. 10/29
    """
    month = random.randint(1,12)
    year = random.randint(15, 50)
    return f"{month}/{year}"
    
def generate_cvv():
    return random.randint(100, 999)


# Generate a list of 100 dummy bins
bins = generate_random_bin(data_length)
df['debit_card_no'] = [generate_debit_card_number(bin) for bin in bins]
df['debit_card_expiry'] = [generate_card_exp_date() for x in range(data_length)]
df['debit_card_cvv'] = [generate_cvv() for x in range(data_length)]


bins = generate_random_bin(data_length)
df['credit_card_no'] = [generate_debit_card_number(bin) for bin in bins]
df['credit_card_expiry'] = [generate_card_exp_date() for x in range(data_length)]
df['credit_card_cvv'] = [generate_cvv() for x in range(data_length)]
# Generate 100 debit card numbers with the dummy bins
# debit_card_numbers = [generate_debit_card_number(bin) for bin in bins]



#bank account number
# Example usage:
countries = ['EU', 'USA']
df['bank_account_no'] = [generate_bank_account_number(random.choice(countries)) for x in range(data_length)]



print(df.head())
print(df.tail())

df.to_csv('dummy_data_generation/sample_output_data_1.csv', index=False)