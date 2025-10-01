from __future__ import annotations

import time
from enum import Enum

import yfinance as yf


class AccountType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"


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


class Account:
    def __init__(self, name: str, balance: float, account_type: AccountType):
        """
        Represents a financial account.

        :param name: The name of the account (e.g., 'Checking', 'Mortgage').
        :param balance: Current balance of the account.
        :param account_type: AccountType.ASSET or AccountType.LIABILITY.
        """
        if not isinstance(account_type, AccountType):
            raise ValueError("account_type must be an instance of AccountType")

        self.name = name
        self.balance = balance
        self.account_type = account_type

    def __repr__(self):
        return f"<Account(name={self.name}, type={self.account_type.value}, balance={self.balance})>"


class User:
    def __init__(self, username: str, currency: Currency):
        """
        Represents a user with multiple accounts.

        :param username: The name of the user.
        """
        self.username = username
        self.currency = currency
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def total_assets(self):
        return sum(
            a.balance for a in self.accounts if a.account_type == AccountType.ASSET
        )

    def total_liabilities(self):
        return sum(
            a.balance for a in self.accounts if a.account_type == AccountType.LIABILITY
        )

    def net_worth(self):
        return self.total_assets() - self.total_liabilities()

    def __repr__(self):
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
        return f"<User(username={self.username}, net_worth={self.net_worth()}{self.currency.symbol})>"
