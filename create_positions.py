import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from pprint import pprint


class Position(object):
    ticker = ""
    std_dev = 0
    last_price = 0
    distribution_yield = 0
    mu = 0
    number_of_shares = 0

    def __init__(self,ticker,distribution_yield,number_of_shares):
        start = dt.datetime(1990, 9, 11)
        end = dt.datetime(2019, 9, 11)
        prices = web.DataReader(ticker, 'yahoo', start, end)['Close']
        returns = prices.pct_change()

        self.ticker = ticker
        self.std_dev = returns.std()
        self.last_price = prices[-1]
        # revisit - pull information in automatically
        self.distribution_yield = distribution_yield
        # approximation - revisit
        self.mu = (( prices[-1] - prices[0] ) / prices[0]) / (end - start).days
        self.number_of_shares
        # add tax-status of distributions at some point
        print('position created')

def create_position(ticker,distribution_yield,number_of_shares):
    return Position(ticker,distribution_yield,number_of_shares)

position = create_position('spy',0.05,100)
pprint(vars(position))