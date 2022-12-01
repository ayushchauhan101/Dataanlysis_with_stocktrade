import pandas as pd

data = pd.read_excel('data.xlsx')
df = pd.DataFrame(data)

# find all occurences of transaction between 200 to 300
filter_by_close = df['Close'].between(200, 300)

filtered_data = df.loc[filter_by_close, ['Ticker', 'Open', 'Close']]

# to create a new excel file only with the desired data
filtered_data.to_excel('new_data.xlsx')
