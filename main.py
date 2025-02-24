# # main.py
# exec(open('data_fetch.py').read())
# exec(open('scoring.py').read())
# exec(open('indicators.py').read())
# exec(open('recommendation.py').read())
# exec(open('backtest.py').read())
# #exec(open('stock_price.py').read())


import os

# Execute data fetching and preprocessing scripts
exec(open('data_fetch.py').read())

# Ask the user to select a risk level
risk_level = input("Select risk level (high, medium, low): ").strip().lower()

# Map risk levels to corresponding file names
risk_files = {
    "high": "scoring_high.py",
    "medium": "scoring_medium.py",
    "low": "scoring_low.py"
}

# Execute the appropriate scoring script
if risk_level in risk_files:
    exec(open(risk_files[risk_level]).read())
else:
    print("Invalid risk level selected. Please choose high, medium, or low.")
    exit(1)

# Continue with other scripts
exec(open('indicators.py').read())
exec(open('recommendation.py').read())
exec(open('backtest.py').read())
