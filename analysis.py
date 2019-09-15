import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

from create_positions import create_position
from create_portfolio import create_portfolio


num_of_simulations = 1000
time_horizon = 252


portfolio = create_portfolio([create_position('XOM',0.05,100),create_position('SPY',0.05,100)])

simulation_df = pd.DataFrame()
for x in range(num_of_simulations):
    
    portfolio_series = []
    
    portfolio_value = portfolio.initial_portfolio_value * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(time_horizon):
        price = price_series[count] * (1 + np.random.normal(mu, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series
    

mean = simulation_df.mean()
average_of_final_outcomes = mean.mean()
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.suptitle('Monte Carlo - SPY')
plt.show()
    
    
#run_monte_carlo()