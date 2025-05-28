# gets stocks data

import yfinance as yf

def get_stock_data(ticker: str, period="5d", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist.to_dict()

def get_current_price(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.info.get('regularMarketPrice', 'N/A')
