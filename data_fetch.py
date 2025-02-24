import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime
import panel as pn
from IPython.display import display

tickers = ["AAPL", "NVDA", "MSFT", "AMZN", "GOOGL","GOOG", "META", "TSLA", "AMD","RKLB"]


# Function to get financial data
def get_financials(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    try:
      
        fcf = info.get("freeCashflow", 0)
        market_cap = info.get("marketCap", 1)  
        return {
            "Ticker": ticker,
            "P/E Ratio": info.get("trailingPE", np.nan),
            "P/B Ratio": info.get("priceToBook", np.nan),
            "EV/EBITDA": info.get("enterpriseToEbitda", np.nan),
            "ROE": info.get("returnOnEquity", np.nan)* 100,
            "Market Cap": market_cap,
            "FCF Yield": fcf / market_cap if market_cap > 0 else np.nan,  
            "Debt/Equity": info.get("debtToEquity", np.nan),
            "Dividend Yield": info.get("dividendYield", np.nan)
        }
    except:
        return None

stock_data = [get_financials(ticker) for ticker in tickers]
df = pd.DataFrame(stock_data) 
df_row = df.copy()
df_perf = df.copy()  
