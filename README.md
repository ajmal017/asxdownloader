# asxdownloader

Since the recent addition of the [yfinance](https://github.com/ranaroussi/yfinance) module developed by the absolute gun @ranaroussi , I thought it made sense to have a marketwide downloading mechanism for a variety of markets. At the moment that is just going to be limited to the ASX as its open when I'm awake. 

The basic premise is fairly simple - download all the ASX stocks and do a filter for nice chart characteristics. In practice it can be made vastly more advanced with the help of an SQL database with a series of abstractions generated by market filters (which I have implemented myself but haven't written as yet for this particular git repo as it is intended to help my friends learn python, higher level math and financial markets simultaneously).

# Usage

Import the module for use in historical data storage

```python
from ASXTesting import asxDownloader

# asxDownloader(0) gives 1 year worth of hourly historical data
# asxDownloader(1) gives 10 years worth of daily historical data
# asxDownloader(2) gives all of the weekly historical data
 ```

# Dependencies
   asxdownloader depends on the yfinance module which can be installed using the bash commands stipulated on the [yfinance](https://github.com/ranaroussi/yfinance) repo.
