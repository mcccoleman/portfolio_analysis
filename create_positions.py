import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


class Position(object):
    ticker = ""
    std_dev = 0
    last_price = 0
    distribution_yield = 0
    mu = 0

    def __init__(self,ticker,distribution_yield):

        start = dt.datetime(1990, 9, 11)
        end = dt.datetime(2019, 9, 11)
        prices = web.DataReader(ticker, 'yahoo', start, end)['Close']
        returns = prices.pct_change()

        self.ticker = self
        self.std_dev = returns.std()
        self.last_price = prices[-1] * (1 + np.random.normal(0, returns.std()))
        self.distribution_yield = distribution_yield
        self.mu = (( prices[-1] - prices[0] ) / prices[0]) / (end - start).days
        print('position created')

def create_position(ticker,distribution_yield):
    return Position(ticker,distribution_yield)

create_position('spy',0.05)