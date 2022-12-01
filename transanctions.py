import pandas as pd

data = pd.read_excel('data.xlsx')
df = pd.DataFrame(data)

filter_by_close = df['Close'].between(200, 300)

filtered_data = df.loc[filter_by_close, ['Ticker', 'Open', 'Close']]
print(filtered_data)

# filtered_data.to_excel('new_data.xlsx')
