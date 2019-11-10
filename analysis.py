import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import create_position
import create_portfolio
import create_account


num_of_simulations = 1000
time_horizon = 252


portfolio = create_portfolio.create_portfolio([create_account.create_account("taxable","taxable",[create_position.create_position('SPY',0.05,100),create_position.create_position('XOM',0.05,100)])])
initial_value = portfolio.initial_portfolio_value()

simulation_df = pd.DataFrame()
for x in range(num_of_simulations):
    count = 0
    portfolio_series = []
    portfolio_value = portfolio.initial_portfolio_value() * (1 + np.random.normal(0, portfolio.portfolio_standard_deviation))
    portfolio_series.append(portfolio_value)
    
    for y in range(time_horizon):
        price = portfolio_series[count] * (1 + np.random.normal(portfolio.calculated_mu(), portfolio.portfolio_standard_deviation))
        portfolio_series.append(price)
        count += 1
        
    simulation_df[x] = portfolio_series
    
mean = simulation_df.mean()
average_of_final_outcomes = mean.mean()
plt.plot(simulation_df)
plt.axhline(y = portfolio.initial_portfolio_value(), color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.suptitle('Monte Carlo - Portfolio')
plt.show()
    
    
run_monte_carlo()