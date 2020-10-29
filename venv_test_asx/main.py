# Install yfinance with the following command
# pip3 install yfinance

import yfinance as yf
zip_ax = yf.Ticker("Z1P.AX")
# msft = yf.Ticker("MSFT")


zip_info = zip_ax.info
#zip_volume = zip_ax.history(period="max")
zip_volume = zip_ax.history(period="6mo")
# .actions, .dividends, .splits
print("breakpoint here")
