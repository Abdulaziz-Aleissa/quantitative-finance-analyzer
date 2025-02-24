# Scoring Functions for Fundamental Analysis
def score_pe(pe):
    """Scores P/E ratio: Lower is better."""
    if pe <= 20: return 5
    elif pe <= 25: return 4
    elif pe <= 30: return 3
    elif pe <= 35: return 3
    else: return 1

def score_pb(pb):
    """Scores P/B ratio: Lower is better."""
    if pb <= 3: return 5
    elif pb <= 4: return 4
    elif pb <= 5: return 3
    elif pb <= 6: return 2
    else: return 1

def score_ev_ebitda(ev_ebitda):
    """Scores EV/EBITDA: Lower is better."""
    if ev_ebitda <= 13: return 5
    elif ev_ebitda <= 16: return 4
    elif ev_ebitda <= 19: return 3
    elif ev_ebitda <= 23: return 2
    else: return 1

def score_roe(roe):
    """Scores Return on Equity (ROE): Higher is better."""
    if roe >= 15: return 5
    elif roe >= 10: return 4
    elif roe >= 5: return 3
    elif roe >= 2: return 2
    else: return 1

def score_rsi(rsi):
    """Scores RSI (Relative Strength Index): Detects overbought/oversold conditions."""
    if rsi < 50: return 5  # Oversold (buy signal)
    elif rsi > 70: return 1  # Overbought (sell signal)
    else: return 3  # Neutral

def score_volatility(volatility):
    """Scores stock volatility: Lower is better for stability."""
    if volatility <= 3: return 5
    elif volatility <= 4: return 4
    elif volatility <= 5: return 3
    elif volatility <= 6: return 2
    else: return 1

# Apply scoring functions
df["P/E Score"] = df["P/E Ratio"].apply(score_pe)
df["P/B Score"] = df["P/B Ratio"].apply(score_pb)
df["EV/EBITDA Score"] = df["EV/EBITDA"].apply(score_ev_ebitda)
df["ROE Score"] = df["ROE"].apply(score_roe)
