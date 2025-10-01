import yfinance as yf

pair = yf.Ticker("EURVND=X")
print(pair.fast_info["last_price"])
print(pair.fast_info["currency"])
