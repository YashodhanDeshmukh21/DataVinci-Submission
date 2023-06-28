import pandas as pd
import yfinance as yf

def extract_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error occurred while extracting data: {e}")
        return None

# Define the stock symbol, start date, and end date
symbol = 'RELIANCE.NS'
start_date = '2022-06-28'
end_date = '2023-06-28'

# Step 1: Extract historical data
stock_data = extract_stock_data(symbol, start_date, end_date)

# Step 2: Calculate additional parameters
stock_data['Return'] = stock_data['Close'].pct_change() * 100
stock_data['Volatility'] = stock_data['Close'].rolling(window=30).std()
stock_data['Market_Cap'] = yf.Ticker(symbol).info.get('marketCap')
stock_data['P_E_Ratio'] = yf.Ticker(symbol).info.get('trailingPE')

# Step 2: Save data to CSV file
if stock_data is not None:
    file_name = f"{symbol}_{start_date}_{end_date}.csv"
    stock_data.to_csv(file_name)
    print(f"Stock data saved to {file_name}")
else:
    print("Error occurred while extracting stock data.")

# Specify the path to the CSV file
file_path = "RELIANCE.NS_2022-06-28_2023-06-28.csv"

# Read the data from the CSV file
data = pd.read_csv(file_path)

data

# Check for missing values in the DataFrame
data.isnull().sum()

mean_return = data['Return'].mean()
data['Return'].fillna(mean_return, inplace=True)

average_volume= data['Volume'].mean()
print("The average daily trading volume:",average_volume)

print(data['Volatility'].min())
print(data['Volatility'].max())

data['Volatility'].fillna(data['Volatility'].mean,inplace=True)

data.isnull().sum()

import matplotlib.pyplot as plt
import numpy as np

# Step 5: Plot volatility vs day 
plt.plot(stock_data.index, stock_data['Volatility'], label='Volatility')
plt.xlabel('Day')
plt.ylabel('Volatility')
plt.title('Volatility vs Day')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

import mplfinance as mpf

start_date = '2022-06-28'
end_date = '2022-07-28'

# Step 1: Extract historical data
stock_data = extract_stock_data(symbol, start_date, end_date)

# Step 2: Create candlestick chart
mpf.plot(stock_data, type='candle', title='Stock Performance', ylabel='Price', style='yahoo')
