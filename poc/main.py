from classes import Account, AccountType, Currency, User

u = User("Kyle", Currency.EUR)

u.add_account(Account("Checking", 5000, AccountType.ASSET))
u.add_account(Account("Savings", 12000, AccountType.ASSET))
u.add_account(Account("Car Loan", 8000, AccountType.LIABILITY))

print(u)  # <User(username=Alice, net_worth=9000)>
print("Assets:", u.total_assets(), u.currency.symbol)
print("Liabilities:", u.total_liabilities(), u.currency.symbol)
print("Net worth:", u.net_worth(), u.currency.symbol)

# Convert 100 EUR → USD
amount_usd = Currency.EUR.convert_to(Currency.USD, 100)
print("100 EUR =", amount_usd, "USD")

# Just get the rate EUR → JPY
rate_eur_jpy = Currency.EUR.get_rate(Currency.YEN)
print("1 EUR =", rate_eur_jpy, "JPY")
