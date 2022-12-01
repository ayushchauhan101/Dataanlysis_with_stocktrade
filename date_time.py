# assigning an alias instead of tyoing pandas everytime
import pandas as pd
# here we are importing df from another .py file within the same directory called parsed_sheet.py
from parsed_sheet import df

# to print the total columns and rows
print(df.shape)
# to print each column and their datatype
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])

# print the day from 10th item from thr Date column
print(df.loc[10, 'Date'].day_name())

# print the day of each entry from the Date column
print(df['Date'].dt.day_name())

# print the day from the earliest entry
print(df['Date'].min().day_name())


