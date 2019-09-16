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
    basis = 0
    last_price = 0
    distribution_yield = 0
    mu = 0
    number_of_shares = 0

    def __init__(self,ticker,distribution_yield,number_of_shares):
        start = dt.datetime(2017, 1, 1)
        end = dt.datetime(2019, 9, 15)
        prices = web.DataReader(ticker, 'yahoo', start, end)['Close']
        returns = prices.pct_change()

        self.ticker = ticker.upper()
        self.position_std_dev = returns.std()
        self.number_of_shares = number_of_shares
        self.basis = prices[-1]
        self.last_price = prices[-1]       

        # approximation - revisit
        self.mu = (( prices[-1] - prices[0] ) / prices[0]) / (end - start).days
        # revisit - pull information
        self.distribution_yield = distribution_yield
         # add tax-status of distributions at some point

    def print_position_attributes(self):
        print('Position Ticker: {ticker}'.format(ticker=self.ticker))
        print('Position Std: {position_std_dev}'.format(position_std_dev=self.position_std_dev))
        print('Position Mu: {mu}'.format(mu=self.mu))
        print('Number of Shares: {number}'.format(number=self.number_of_shares))
        print('Yield: {dis_yield}'.format(dis_yield=self.distribution_yield))
        print('')

def create_position(ticker,distribution_yield,number_of_shares):
    return Position(ticker,distribution_yield,number_of_shares)

position = create_position('spy',0.05,100)
