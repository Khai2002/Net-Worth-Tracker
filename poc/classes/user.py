from .account import Account, AccountType
from .currency import Currency


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
