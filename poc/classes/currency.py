from __future__ import annotations

import time
from enum import Enum

import yfinance as yf


class Currency(Enum):
    YEN = ("JPY", "¥")
    EUR = ("EUR", "€")
    VND = ("VND", "₫")
    USD = ("USD", "$")

    def __init__(self, code: str, symbol: str):
        self.code = code
        self.symbol = symbol

    def __str__(self):
        return f"{self.symbol} ({self.code})"

    def get_rate(self, target: Currency, retries: int = 3, delay: float = 1.0) -> float:
        """
        Get exchange rate from this currency to the target currency
        using yfinance fast_info.
        """
        ticker_name = f"{self.code}{target.code}=X"
        ticker = yf.Ticker(ticker_name)

        for attempt in range(retries):
            try:
                rate = ticker.fast_info["last_price"]
                return rate
            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    raise RuntimeError(f"Failed to fetch rate for {ticker_name}: {e}")

    def convert_to(self, target: Currency, amount: float) -> float:
        """
        Convert an amount from this currency to the target currency.
        """
        rate = self.get_rate(target)
        return amount * rate
