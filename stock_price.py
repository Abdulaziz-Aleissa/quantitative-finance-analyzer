# Function to get stock price data
def get_stock_prices(ticker, period="3y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df["Close"]

# Fetch price data for selected stocks
df_prices = pd.DataFrame()
for ticker in tickers:
    df_prices[ticker] = get_stock_prices(ticker)

# Fetch S&P 500 historical price data
sp500_prices = get_stock_prices("^GSPC")
df_prices["S&P 500"] = sp500_prices

# Create Interactive Plotly Figure for Stock Prices
fig_price = go.Figure()

# Add each stock's price history to the plot
for stock in df_prices.columns:
    fig_price.add_trace(go.Scatter(
        x=df_prices.index, 
        y=df_prices[stock], 
        mode="lines",
        name=stock
    ))

# Customize layout
fig_price.update_layout(
    title="Stock Price Chart: Selected Stocks vs. S&P 500",
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    hovermode="x unified",
    template="presentation",
    width=1000,
    height=600
)

# Show interactive plot
pn.extension()
popup_price = pn.panel(fig_price, width=2560, height=1440)
popup_price.show()