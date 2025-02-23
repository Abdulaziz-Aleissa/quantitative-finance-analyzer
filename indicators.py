# Function to calculate stock price volatility
def get_volatility(ticker, period="3y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return np.std(df["Close"].pct_change()) * 100  # Convert to percentage

# Calculate and score volatility
df["Volatility (%)"] = df["Ticker"].apply(get_volatility)
df["Volatility Score"] = df["Volatility (%)"].apply(score_volatility)

# Function to calculate RSI (Relative Strength Index)
def get_rsi(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs)).iloc[-1]  # Last RSI value

# Calculate and score RSI
df["RSI"] = df["Ticker"].apply(get_rsi)
df["RSI Score"] = df["RSI"].apply(score_rsi)

# Compute Final Score by summing all scores
df["Final Score"] = (
    df["P/E Score"] + df["P/B Score"] + df["EV/EBITDA Score"] +
    df["ROE Score"] + df["RSI Score"] + df["Volatility Score"]
)
