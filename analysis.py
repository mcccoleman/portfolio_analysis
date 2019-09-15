import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



#def run_monte_carlo():
style.use('ggplot')

start = dt.datetime(1990, 9, 11)
end = dt.datetime(2019, 9, 11)


prices = web.DataReader('SPY', 'yahoo', start, end)['Close']
returns = prices.pct_change()

first_price = prices[0]
last_price = prices[-1]
price_change = ( last_price - first_price ) / first_price
number_of_days = (end - start).days
    #number_of_days = 504
mu = price_change / number_of_days





    # number of trials
num_of_simulations = 1000
    # number of days 
time_horizon = 252


simulation_df = pd.DataFrame()
for x in range(num_of_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
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