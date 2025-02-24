# Scoring Functions for Fundamental Analysis
def score_pe(pe):
    """Scores P/E ratio: Lower is better."""
    if pe <= 10: return 5
    elif pe <= 15: return 4
    elif pe <= 20: return 3
    elif pe <= 25: return 2
    else: return 1

def score_pb(pb):
    """Scores P/B ratio: Lower is better."""
    if pb <= 1: return 5
    elif pb <= 2: return 4
    elif pb <= 3: return 3
    elif pb <= 4: return 2
    else: return 1

def score_ev_ebitda(ev_ebitda):
    """Scores EV/EBITDA: Lower is better."""
    if ev_ebitda <= 8: return 5
    elif ev_ebitda <= 10: return 4
    elif ev_ebitda <= 12: return 3
    elif ev_ebitda <= 15: return 2
    else: return 1

def score_roe(roe):
    """Scores Return on Equity (ROE): Higher is better."""
    if roe >= 30: return 5
    elif roe >= 20: return 4
    elif roe >= 15: return 3
    elif roe >= 10: return 2
    else: return 1

def score_rsi(rsi):
    """Scores RSI (Relative Strength Index): Detects overbought/oversold conditions."""
    if rsi < 30: return 5  # Oversold (buy signal)
    elif rsi > 70: return 1  # Overbought (sell signal)
    else: return 3  # Neutral

def score_volatility(volatility):
    """Scores stock volatility: Lower is better for stability."""
    if volatility <= 1: return 5
    elif volatility <= 2: return 4
    elif volatility <= 3: return 3
    elif volatility <= 4: return 2
    else: return 1

# Apply scoring functions
df["P/E Score"] = df["P/E Ratio"].apply(score_pe)
df["P/B Score"] = df["P/B Ratio"].apply(score_pb)
df["EV/EBITDA Score"] = df["EV/EBITDA"].apply(score_ev_ebitda)
df["ROE Score"] = df["ROE"].apply(score_roe)
