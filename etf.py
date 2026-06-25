import yfinance as yf

def get_etf(ticker):
    hist = yf.Ticker(ticker).history(period="5d")

    today = hist["Close"].iloc[-1]
    prev = hist["Close"].iloc[-2]

    change = today - prev
    pct = (change / prev) * 100

    return today, change, pct
