# Recommendation System
def recommend_stocks(df):
    recommendations = []
    for _, row in df.iterrows():
        rec = "Hold"
        explanation = "Stock has balanced valuation and performance."
        if row["Final Score"] >= 25 or row["RSI"] < 30:
            rec = "Buy"
            explanation = "Stock is undervalued with strong fundamentals and is oversold."
        elif row["Final Score"] <= 10 or row["RSI"] > 70:
            rec = "Sell"
            explanation = "Stock is overvalued and overbought, signaling a potential correction."
        recommendations.append({
            "Ticker": row["Ticker"],
            "Recommendation": rec,
            "P/E Score": row["P/E Score"],
            "P/B Score": row["P/B Score"],
            "EV/EBITDA Score": row["EV/EBITDA Score"],
            "ROE Score": row["ROE Score"],
            "RSI Score": row["RSI Score"],
            "Volatility Score": row["Volatility Score"],
            "Final Score": row["Final Score"],
            "RSI": row["RSI"],
        })
    return pd.DataFrame(recommendations)

recommendations = recommend_stocks(df)
print("\nStock Recommendations:")
display(df_row)
display(recommendations)
