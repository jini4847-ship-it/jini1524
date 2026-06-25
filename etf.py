import yfinance as yf

def get_etf(ticker):
    hist = yf.Ticker(ticker).history(period="10d")

    close = hist["Close"].dropna()

    if len(close) < 2:
        return None, None, None

    today = close.iloc[-1]
    prev = close.iloc[-2]

    change = today - prev
    pct = (change / prev) * 100

    return round(today, 2), round(change, 2), round(pct, 2)