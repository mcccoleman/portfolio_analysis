import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


class Position(object):
    ticker = ""
    distribution_yield = 0
    mu = 0

    def __init___(self,ticker,last_price,distribution_yield):

        start = dt.datetime(1990, 9, 11)
        end = dt.datetime(2019, 9, 11)
        prices = web.DataReader(ticker, 'yahoo', start, end)['Close']
        returns = prices.pct_change()
        first_price = prices[0]
        last_price = prices[-1]
        price_change = ( last_price - first_price ) / first_price
        number_of_days = (end - start).days
        mu = price_change / number_of_days

        self.ticker = self
        self.std_dev = returns.std()
        self.last_price = last_price * (1 + np.random.normal(0, daily_vol))
        self.distribution_yield = distribution_yield
        self.mu = mu

def create_position(ticker,last_price,distribution_yield):
    position = Position(ticker,last_price,distribution_yield)
    return position