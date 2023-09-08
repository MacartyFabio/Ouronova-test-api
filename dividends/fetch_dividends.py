import yfinance as yf
from dividends.models import Dividend  

def fetch_and_save_dividends():
    ticker = "PETR4.SA"

    stock = yf.Ticker(ticker)
    dividends = stock.dividends

    for index, row in dividends.iterrows():
        dividend = Dividend(
            symbol=ticker,
            year=index.year,
            amount=row,
            payment_date=index.date()
        )
        dividend.save()

if __name__ == "__main__":
    fetch_and_save_dividends()
