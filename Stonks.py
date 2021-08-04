import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price Webapp

Shown are the stock closing price and volume of Amazon!

""")

#Defining the ticker Symbol
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#getting historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2011-7-31', end='2021-7-31')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)