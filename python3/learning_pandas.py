from tarfile import data_filter
from xml.etree.ElementInclude import include
import pandas as pd

titanic_df = pd.read_csv("python3/titanic.csv")

print(titanic_df.head())

# data type to be included
print(titanic_df.describe(include=[int, float]))

# overall of dataframe
print(titanic_df.info())

# length of rows
print(len(titanic_df))

# min length and dictionary wise on column labels e.g age < sex
print(min(titanic_df))   

# matrix shape
print(titanic_df.shape)

# type of index of dataframe
print(titanic_df.index)

# to get column names
print(titanic_df.columns)

# to get stats on data
print(titanic_df.min(numeric_only=True))

print(titanic_df.mean(numeric_only=True))

# to sort the dataframe
print(titanic_df.sort_values(by='age', ascending=True).head(5))