import pandas as pd             # dataframe
import seaborn as sns            # plots
import matplotlib.pyplot as plt   # plots
import yfinance as yf

#  SET ticker, yf_period and yf_interval
#  ticker - securities to download
ticker = ["aapl", "FBgrx", "qqq", "VBTLX", 'twtr', 'FLT', '^dji']

#  set market indexes to compare equities with
market_index = ['^DJI', '^IXIC', '^GSPC']  # Dow Jones, Nasdaq and S&P500

#  time period and interval
yf_period = "1y"   # 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
yf_interval = "1d"    # 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo


#  print set parameters
print('TICKER:\t\t{}'.format(ticker))
print('MARKET INDEX:\t{}'.format(market_index))
print('PERIOD:\t\t{}'.format(yf_period))
print('INTERVAL:\t{}'.format(yf_interval))

data = yf.download(
    tickers= "aapl",
    period="ytd",
    interval="1d",
    group_by='ticker',
    auto_adjust=True,
    prepost=True,
    threads=True,
    proxy=None
)

