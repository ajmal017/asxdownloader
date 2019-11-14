import yfinance as yf
import pandas as pd
import requests
import os

from collections import OrderedDict
import operator
from indicators import *
from marketScans import *

url = 'https://www.asx.com.au/asx/research/ASXListedCompanies.csv'
market = pd.read_csv(url,header=1)

aussie = ''
for i in range(0,len(market)):
	aussie = aussie + market['ASX code'][i] + '.AX' + ' '

pathHourly = os.path.expanduser('~') + '/TradingHistoryASX/Hourly/'
pathDaily = os.path.expanduser('~') + '/TradingHistoryASX/Daily/'
pathWeekly = os.path.expanduser('~') + '/TradingHistoryASX/Weekly/'

period = ['2y','10y','max']
path = [pathHourly,pathDaily,pathWeekly]
interval = ['1h','1d','1wk']

# Using the index of 0, 1 and 2 we can respectively select the entries in period, path and interval that correspond with
# the desired file path, ticker length and historical data duration that we would like to download
#
# e.g. to download 2 years worth of hourly ASX historical data we simply set x = 0 when running our download function: asxDownloader(0)
# to download 10 years worth of daily ASX historical data we simply set x = 1 when running our download function: asxDownloader(1)
# to download all of the weekly ASX historical data we simply set x = 2 when running our download function: asxDownloader(2)

def asxDownloader(x):
	#if the path does not exist in the home folder, create it with try/except
	try:
		os.stat(path[x])
	except:
		os.mkdir(path[x]) 

	data = yf.download(# or pdr.get_data_yahoo(...
            # tickers list or string as well
			tickers = aussie,

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
			period = period[x],

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
			interval = interval[x],

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
			group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
			auto_adjust = True,

            # download pre/post regular market hours data
            # (optional, default is False)
			prepost = True,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
			threads = True,

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
			proxy = None
        )

	for i in range(0,len(market)):
		data[market['ASX code'][i] + '.AX'].to_csv(path[x] + market['ASX code'][i] + '_AX.csv',encoding='utf-8')
