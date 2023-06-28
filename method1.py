import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

def extract_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error occurred while extracting data: {e}")
        return None

def calculate_average_volume(data):
    if data is None:
        return None
    average_volume = data['Volume'].mean()
    return average_volume

def visualize_stock_performance(data):
    if data is None:
        return
    mpf.plot(data, type='candle', volume=True, show_nontrading=False)

# Define the stock symbol, start date, and end date
symbol = 'RELIANCE.NS'
start_date = '2022-06-28'
end_date = '2023-06-28'

# Step 1: Extract historical data
stock_data = extract_stock_data(symbol, start_date, end_date)

# Step 2: Process the data
average_volume = calculate_average_volume(stock_data)
if average_volume:
    print(f"Average Daily Trading Volume: {average_volume}")

# Step 3: Visualize the data
visualize_stock_performance(stock_data)
