import streamlit as st
import yfinance as yf
import pandas as pd

# Set the title of the web app
st.title('Stock Price Web Application')

# Create a text input for the stock ticker
ticker_symbol = st.text_input("Enter Stock Ticker Symbol", "AAPL")

# Define a function to fetch stock data
def fetch_stock_data(ticker):
    stock_data = yf.Ticker(ticker)
    # Get historical market data
    df = stock_data.history(period="1y")  # Fetch data for the last year
    return df

# Button to fetch the stock data
if st.button('Get Stock Price'):
    df = fetch_stock_data(ticker_symbol)
    
    # Display the stock data
    st.subheader(f'Stock Data for {ticker_symbol}')
    st.line_chart(df['Close'])  # Show closing prices

    # Show the data in a table
    st.dataframe(df)
