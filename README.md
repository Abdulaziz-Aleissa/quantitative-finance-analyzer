# Stock Recommendation & Backtesting Project



## Overview

This project is a simple stock recommendation system and backtesting tool using **[yfinance](https://pypi.org/project/yfinance/)** for data retrieval. It:

1. Fetches stock and fundamental data from Yahoo Finance.  
2. Calculates various ratios, scores, and technical indicators (P/E, P/B, EV/EBITDA, ROE, RSI, Volatility, etc.).  
3. Produces a **Final Score** combining fundamental and technical metrics.  
4. Recommends **Buy**, **Sell**, or **Hold** based on the Final Score and RSI thresholds.  
5. Generates a performance plot (backtest) comparing selected stocks vs. the S&P 500.

The entire workflow is modularized into separate Python scripts for clarity and maintainability.

---

## Files and Their Roles

1. **`data_fetch.py`**  
   - **Purpose**: Fetches financial data for a list of tickers using `yfinance`.  
   - **Key Functions**:  
     - `get_financials(ticker)`: Returns a dictionary with P/E, P/B, EV/EBITDA, ROE, Market Cap, FCF Yield, Debt/Equity, and Dividend Yield.  
   - **Usage**:  
     - Creates a DataFrame (`df`) containing fundamental metrics for each ticker in the `tickers` list.  

2. **`scoring.py`**  
   - **Purpose**: Assigns *fundamental analysis scores* for each metric retrieved in `data_fetch.py`.  
   - **Key Functions**:
     - `score_pe(pe)`, `score_pb(pb)`, `score_ev_ebitda(ev_ebitda)`, `score_roe(roe)`, `score_rsi(rsi)`, `score_volatility(volatility)`.  
   - **Usage**:  
     - Each ratio/indicator is assigned a numeric score based on thresholds (e.g., lower P/E => higher score, lower volatility => higher score).  
     - Appends **P/E Score**, **P/B Score**, **EV/EBITDA Score**, **ROE Score** columns to `df`.  

3. **`indicators.py`**  
   - **Purpose**: Calculates *technical indicators* (RSI, volatility), then applies scoring logic.  
   - **Key Functions**:  
     - `get_volatility(ticker, period="2wk")`: Computes standard deviation of 2-week daily returns (converted to a percentage).  
     - `get_rsi(ticker, period="2wk")`: Calculates the 14-period RSI from 2-week daily price data.  
     - Calculates overall **Final Score** by summing all relevant scores (fundamental + technical).  
   - **Usage**:  
     - Appends **Volatility (%)**, **RSI**, **Volatility Score**, **RSI Score**, and **Final Score** to `df`.  

4. **`recommendation.py`**  
   - **Purpose**: Uses the final metrics and scores to produce a **Buy**, **Sell**, or **Hold** recommendation.  
   - **Key Logic**:  
     - **Buy** if `Final Score >= 25` **and** `RSI < 30` (strong fundamentals + oversold).  
     - **Sell** if `Final Score <= 10` **and** `RSI > 70` (weak fundamentals + overbought).  
     - **Hold** otherwise.  
   - **Usage**:  
     - Returns a DataFrame (`recommendations`) with each ticker’s recommended action and relevant scores.  

5. **`backtest.py`**  
   - **Purpose**: Fetches historical price data and plots performance (cumulative returns) for each stock vs. the S&P 500.  
   - **Key Functions**:  
     - `get_stock_performance(ticker, period="3y")`: Retrieves 3-year historical data and calculates cumulative return.  
   - **Usage**:  
     - Creates an interactive Plotly line chart showing each ticker’s return vs. `^GSPC` (the S&P 500).  
   - **Note**: Uses `panel` to create an interactive pop-up plot if run in a suitable environment.  

6. **`main.py`**  
   - **Purpose**: The **entry point** for the entire project.  
   - **Process**:  
     1. Runs `data_fetch.py` to load fundamental data into `df`.  
     2. Runs `scoring.py` to apply fundamental scoring.  
     3. Runs `indicators.py` to compute RSI, volatility, and the final score.  
     4. Runs `recommendation.py` to produce the recommendation table.  
     5. Runs `backtest.py` to display an interactive performance chart comparing selected tickers vs. the S&P 500.  
   - **Usage**:  
     - Simply run `python main.py` and the console will display both the fundamental data table and the recommendation table.  
     - A pop-up chart will appear if supported by your environment.

---

## Installation & Requirements

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/Abdulaziz-Aleissa/quantitative-finance-analyzer.git
   cd stock-recommendation

2. **Download** Required libraries:
   ```bash
   pip install -r requirements.txt

3. **Run** the script:
   ```bash
   python main.py


## Example Table:

![Alt Text](/Example1.png)

## Example Plot:

![Alt Text](/Example2.png)


## Disclaimer

This project is provided **"as is"** without any warranties or guarantees of any kind. The author is not responsible for any damages, data loss, or issues that may arise from using this code. Use this project at your own risk.

### Not Financial Advice

The information, models, and tools provided in this repository are for **educational and informational purposes only**. Nothing in this repository constitutes financial, investment, trading, or legal advice. 

You should **not** rely on any predictions, outputs, or recommendations made by this project to make financial decisions. Always **do your own research** and consult a qualified financial advisor before making any investment or trading decisions.

By using this repository, you acknowledge and agree that the maintainers are **not liable** for any financial losses or consequences that may result from using this code.


   
