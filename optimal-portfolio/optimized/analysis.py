import pandas as pd
import matplotlib.pyplot as plt
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.expected_returns import ema_historical_return
from pypfopt.risk_models import exp_cov
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.plotting import plot_efficient_frontier
from pypfopt.plotting import plot_weights
from pypfopt.cla import CLA
import numpy as np
import seaborn as sns

# References
# https://pyportfolioopt.readthedocs.io/en/latest/ExpectedReturns.html

MARKET_DAYS_PER_YEAR = 252


data = pd.read_csv('./position_adjusted_close.csv', header= 0, index_col=False)
df = data.set_index('date')
positions = list(df.columns)
returns = df.pct_change()
mean_returns = returns.mean()

vol_ef = []
mu = expected_returns.ema_historical_return(returns, returns_data = True, span = 500)
sigma = risk_models.exp_cov(returns, returns_data = True, span = 180)

def runner():
    ret_ef = np.arange(0, 0.17, 0.01)

    ef = EfficientFrontier(mu, sigma)
    weights = ef.max_sharpe()
    # plot_weights(weights)
    ef.portfolio_performance(verbose = True)


runner()