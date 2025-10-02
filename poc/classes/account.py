from __future__ import annotations

from enum import Enum


class AccountType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"


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
