# Install yfinance with the following command
# pip3 install yfinance

import yfinance as yf
zip_ax = yf.Ticker("Z1P.AX")
# msft = yf.Ticker("MSFT")


zip_info = zip_ax.info
zip_volume = zip_ax.history(period="max")
# .actions, .dividends, .splits
print("breakpoint here")


#
#zipdata = zip.history(period='12mo')
#zipdata.loc[:, 'Volume']
#zipvol = zipdata.loc[:,'Volume']
#zipvol.values
