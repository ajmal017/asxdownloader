import os
import operator
from indicators import movingAverage

def MAscanner(short,multiple,window,path):
    tickers = []
    percentages = []
    long = short * multiple

    for i in range(len(os.listdir(path))):
        x = pd.read_csv(path + os.listdir(path)[i])
        y = [x['Close']]
        gap = movingAverage(x, short)['MA_' + str(short)][-window:] - movingAverage(x, long)['MA_' + str(long)][-window:]

        if all(i for i in gap > 0):
            tickers.append(os.listdir(path)[i])
            percentages.append(100*(x['Close'][len(x)-1] - x['Close'][len(x)-window])/x['Close'][len(x)-window])

    performers = dict(zip(tickers, percentages))
    #performers = [(k, performers(k)) for k in sorted(performers, key = performers.get, reverse = True)]
    performers = sorted(performers.items(), key=operator.itemgetter(1), reverse=True)
    return performers
