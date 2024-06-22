import pandas as pd
import testing_functions as tf

# Example class_df
data = {
    'metadata_rules': [r'key\d+', r'item_\d+', r'account_\d+'],
    'data_rules': [r'\d{8,20}', r'(?:\d{4}[-\s]?){3}\d{4}', r'\b([3-9]\d{2})\b']
}
class_df = pd.DataFrame(data)

# Example source_data
source_data = {
    'key123': ['12345678'],
    'item_456': ['1234-5678-9012-3456'],
    'account_789': ['750']
}

# Example class_df with 15 rules
data = {
    'metadata_rules': [
        r'bank_acc_\d+', r'credit_card_\d+', r'debit_card_\d+', r'credit_score_\d+', r'transaction_\d+', 
        r'salary_\d+', r'pension_\d+', r'med_cond_\d+', r'med_hist_\d+', r'health_ins_\d+', 
        r'disabilities_\d+', r'allergies_\d+', r'employee_\d+', r'order_\d+', r'invoice_\d+'
    ],
    'data_rules': [
        r'\d{8,20}', r'(?:\d{4}[-\s]?){3}\d{4}', r'(?:\d{4}[-\s]?){3}\d{4}', r'\b([3-9]\d{2})\b', 
        r'[A-Z]{2,4}-\d{6,12}', r'\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?', r'\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?', 
        r'[A-Za-z\s,-]{3,100}', r'[A-Za-z\s,-]{3,500}', r'[A-Za-z0-9\s,-]{3,50}', 
        r'[A-Za-z\s,-]{3,100}', r'[A-Za-z\s,-]{3,100}', r'\d{6,10}', r'\d{5}', r'\d{5}'
    ]
}
class_df = pd.DataFrame(data)

# Example source_data with 20 entries
source_data = {
    'bank_acc_12345': ['12345678'],
    'credit_card_67890': ['1234-5678-9012-3456'],
    'debit_card_54321': ['9876 5432 1098 7654'],
    'credit_score_13579': ['750'],
    'transaction_24680': ['TX-123456'],
    'salary_11223': ['100,000.00'],
    'pension_33445': ['50,000'],
    'med_cond_55667': ['Hypertension'],
    'med_hist_77889': ['Asthma and Hypertension'],
    'health_ins_99000': ['ABC12345'],
    'disabilities_11122': ['Visual Impairment'],
    'allergies_33344': ['Peanut Allergy'],
    'employee_55566': ['123456'],
    'order_77788': ['67890'],
    'invoice_99900': ['54321'],
    'bank_acc_23456': ['23456789'],
    'credit_card_78901': ['3456-7890-1234-5678'],
    'debit_card_65432': ['8765 4321 0987 6543'],
    'credit_score_24680': ['800'],
    'transaction_13579': ['TR-654321']
}



# Call the function
result = tf.match_data1(class_df, source_data, match_type='meta')
for key,values in result.items():
    print(key, values)

print()
print("#"*20)
print()

# result = tf.find_best_match_extended(class_df, source_data, match_type='both')
# for key,values in result.items():
#     print(key, values)
