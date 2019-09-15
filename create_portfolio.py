from create_positions import create_position
from pprint import pprint
import numpy as np
import pandas as pd
import pandas_datareader as web
from datetime import datetime
import matplotlib.pyplot as plt


class Portfolio(object):
    positions = []


    def __init__(self,positions):
        self.positions = positions



        # determine covariance of each of the asset classes in portfolio to calculate standrad deviation
        df = pd.DataFrame()
        for stock in self.portfolio_ticker_symbols():
            df[stock] = web.DataReader(stock, data_source='yahoo',start='2017-1-1' ,end='2019-9-15')['Adj Close']
        cov_matrix_daily = df.pct_change().cov()
        # currently only calculating daily for simulations, below will calculate annualized 
        # cov_matrix_annualized = cov_matrix_daily * 252
        # cov_matrix_annualized = cov_matrix_daily
        weights = np.array(self.portfolio_weights())
        self.portfolio_standard_deviation = np.sqrt(np.dot(weights.T, np.dot(cov_matrix_daily, weights)))

    def loop_through_each_position(self):
        counter = 1
        for position in self.positions:
            print('Position Number {counter}'.format(counter=counter))
            counter+=1
            position.print_position_attributes()

    def initial_portfolio_value(self):
        value = 0
        for position in self.positions:
            value += ( position.number_of_shares * position.initial_price)
        return value
    
    def calculated_portfolio_weighted_mu(self):
        weightedMu = 0
        for position in self.positions:
            weightedMu += ( (position.number_of_shares * position.initial_price) / self.initial_portfolio_value() ) * position.mu
        return weightedMu

    def portfolio_ticker_symbols(self):
        symbols = []
        for position in self.positions:
            symbols.append(position.ticker)
        return symbols

    def portfolio_weights(self):
        weights = []
        for position in self.positions:
            weights.append((position.initial_price * position.number_of_shares) / self.initial_portfolio_value())
        return weights

def create_portfolio(positions):
    return Portfolio(positions)
