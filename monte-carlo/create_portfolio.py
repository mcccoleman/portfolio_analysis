from create_position import create_position
from pprint import pprint
import numpy as np
import pandas as pd
import pandas_datareader as web
from datetime import datetime
import matplotlib.pyplot as plt


class Portfolio(object):
    accounts = []


    def __init__(self,accounts):
        self.accounts = accounts
        df = pd.DataFrame()
        for stock in self.portfolio_ticker_symbols():
            df[stock] = web.DataReader(stock, data_source='yahoo',start='2017-1-1' ,end='2019-9-15')['Adj Close']
        cov_matrix_daily = df.pct_change().cov()
        weights = np.array(self.portfolio_weights())
        self.portfolio_standard_deviation = np.sqrt(np.dot(weights.T, np.dot(cov_matrix_daily, weights)))

    def loop_through_each_position(self):
        counter = 1
        for account in self.accounts:
            for position in account.positions:
                print('Position Number {counter}'.format(counter=counter))
                counter+=1
                position.print_position_attributes()

    def initial_portfolio_value(self):
        value = 0
        for account in self.accounts:
            for position in account.positions:
                value += ( position.number_of_shares * position.basis)
        return value
    
    def calculated_mu(self):
        weightedMu = 0
        for account in self.accounts:
            for position in account.positions:
                weightedMu += ( (position.number_of_shares * position.basis) / self.initial_portfolio_value() ) * position.mu
        return weightedMu

    def calculated_std(self):
        df = pd.DataFrame()
        for stock in self.portfolio_ticker_symbols():
            df[stock] = web.DataReader(stock, data_source='yahoo',start='2017-1-1' ,end='2019-9-15')['Adj Close']
        cov_matrix_daily = df.pct_change().cov()
        weights = np.array(self.portfolio_weights())
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix_daily, weights)))

    def calculate_anticipated_portfolio_value_given_position_values(self):
        value = 0
        for account in self.accounts:
            for position in account.positions:
                value += position.calculate_updated_value()
        return value

    def portfolio_ticker_symbols(self):
        symbols = []
        for account in self.accounts:
            for position in account.positions:
                symbols.append(position.ticker)
        return symbols

    def portfolio_weights(self):
        weights = []
        for account in self.accounts:
            for position in account.positions:
                weights.append((position.basis * position.number_of_shares) / self.initial_portfolio_value())
        return weights

def create_portfolio(positions):
    return Portfolio(positions)
