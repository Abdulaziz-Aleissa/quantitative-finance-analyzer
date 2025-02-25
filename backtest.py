# Function to get stock performance (Cumulative Return)
def get_stock_performance(ticker, period="3y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df["Cumulative Return"] = ((1 + df["Close"].pct_change()).cumprod() - 1) * 100
    return df["Cumulative Return"]

# Fetch performance data for selected stocks
df_perf = pd.DataFrame()
for ticker in tickers:
    df_perf[ticker] = get_stock_performance(ticker)

# Fetch S&P 500 historical performance
sp500 = get_stock_performance("^GSPC")  # S&P 500 index ticker in Yahoo Finance
df_perf["S&P 500"] = sp500

# Create Interactive Plotly Figure
fig = go.Figure()

for stock in df_perf.columns:
    fig.add_trace(go.Scatter(
        x=df_perf.index, 
        y=df_perf[stock], 
        mode="lines",
        name=stock
    ))

# Customize layout
fig.update_layout(
    title="Backtest: Performance of Selected Stocks vs. S&P 500",
    xaxis_title="Date",
    yaxis_title="Cumulative Returns",
    hovermode="x unified",
    template="presentation",  # Dark theme for better visibility
    width=1000,  # Set width in pixels
    height=600   # Set height in pixels
)

# Show interactive plot
#fig.show()
pn.extension()
popup = pn.panel(fig, width=1000, height=600)
popup.show()
