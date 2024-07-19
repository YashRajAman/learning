import random

def generate_bank_account_number(country):
    if country == 'EU':
        # EU bank account number format: XXXX XXXX XXXX XXXX
        account_number = ''.join(random.choice('0123456789') for _ in range(16))
        checksum = calculate_eu_checksum(account_number)
        account_number = account_number[:4] + ' ' + account_number[4:8] + ' ' + account_number[8:12] + ' ' + account_number[12:]
    elif country == 'USA':
        # USA bank account number format: XXXX XXXX XXXX
        account_number = ''.join(random.choice('0123456789') for _ in range(12))
        checksum = calculate_usa_checksum(account_number)
        account_number = account_number[:4] + ' ' + account_number[4:8] + ' ' + account_number[8:]
    else:
        raise ValueError("Invalid country specified. Please specify either 'EU' or 'USA'.")

    return account_number + ' ' + str(checksum)

def calculate_eu_checksum(account_number):
    # Simple checksum calculation for EU bank account numbers
    weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    total = sum(int(digit) * weight for digit, weight in zip(account_number, weights))
    return total % 10

def calculate_usa_checksum(account_number):
    # Simple checksum calculation for USA bank account numbers
    weights = [3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7, 1]
    total = sum(int(digit) * weight for digit, weight in zip(account_number, weights))
    return total % 10
