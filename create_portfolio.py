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



        # calculate portfolio standard deviation as part of object creation
        # will involve calculating the correlation with each of the asset classes in portfolio


    def loop_through_each_position(self):
        counter = 1
        for position in self.positions:
            print('Position Number {counter}'.format(counter=counter))
            counter+=1
            position.print_position_attributes()

    def initial_portfolio_value(self):
        current_value = 0
        for position in self.positions:
            current_value += ( position.number_of_shares * position.initial_price)
    
    def portfolio_ticker_symbols(self):
        symbols = []
        for position in self.positions:
            symbols.append(position.ticker)
        print(symbols)
        return symbols

def create_portfolio(positions):
    return Portfolio(positions)


portfolio = create_portfolio([create_position('spy',0.05,100),create_position('XOM',0.05,100)])
portfolio.loop_through_each_position()
portfolio.portfolio_ticker_symbols()
# pprint(vars(portfolio))
