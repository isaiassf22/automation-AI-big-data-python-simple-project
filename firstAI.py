import yfinance as yf


dados = yf.Ticker("PETR4.SA").history("2y")

print(dados.head())