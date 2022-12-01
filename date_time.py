import pandas as pd
from parsed_sheet import df

# print(df.shape)
# print(df.info())

# the column Date will be converted to acceptable datetime
# not needed with this Excel sheet
# df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d %I/%p')

# print the day from 10th item from thr Date column
# print(df.loc[10, 'Date'].day_name())

# print the day of each entry from the Date column
# print(df['Date'].dt.day_name())

# print the day from the earliest entry
# print(df['Date'].min().day_name())


