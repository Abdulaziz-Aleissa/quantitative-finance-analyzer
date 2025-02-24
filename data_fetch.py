import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime
import panel as pn
from IPython.display import display

tickers = ["AAPL", "NVDA", "MSFT", "AMZN", "GOOGL","GOOG", "META", "TSLA", "AMD","RKLB"]

#tickers = ["1150.SR", "1120.SR", "4338.SR", "7010.SR", "2222.SR"]
# Function to get financial data
def get_financials(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    try:
        # Extract relevant financial metrics
        fcf = info.get("freeCashflow", 0)
        market_cap = info.get("marketCap", 1)  # Avoid division by zero
        return {
            "Ticker": ticker,
            "P/E Ratio": info.get("trailingPE", np.nan),
            "P/B Ratio": info.get("priceToBook", np.nan),
            "EV/EBITDA": info.get("enterpriseToEbitda", np.nan),
            "ROE": info.get("returnOnEquity", np.nan)* 100,
            "Market Cap": market_cap,
            "FCF Yield": fcf / market_cap if market_cap > 0 else np.nan,  # Free Cash Flow Yield
            "Debt/Equity": info.get("debtToEquity", np.nan),
            "Dividend Yield": info.get("dividendYield", np.nan)
        }
    except:
        return None

# Fetch data for all stocks
stock_data = [get_financials(ticker) for ticker in tickers]
df = pd.DataFrame(stock_data) # Remove missing values
df_row = df.copy()
df_perf = df.copy()  # Keep a separate copy for backtesting
