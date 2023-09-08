import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

import yfinance as yf
from dividends.models import Dividends

def fetch_and_save_dividends():
    ticker = "PETR4.SA"

    stock = yf.Ticker(ticker)
    dividends = stock.dividends

    for date, dividend_amount in dividends.items():
        year = date.year
        dividend, created = Dividends.objects.get_or_create(
            symbol=ticker,
            date=date,
            defaults={'dividend_amount': dividend_amount}
        )

        if not created:
            dividend.dividend_amount = dividend_amount
            dividend.save()
if __name__ == "__main__":
    fetch_and_save_dividends()
