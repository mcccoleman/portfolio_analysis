import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import quandl
import scipy.optimize as sco

positions = ['AAPL', 'AMZN', 'GOOGL', 'XOM']
market_days_per_year = 252


def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights) * market_days_per_year
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))
                  ) * np.sqrt(market_days_per_year)
    return std, returns


def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((3, num_portfolios))

    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(4)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(
            weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


def display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, weights = random_portfolios(
        num_portfolios, mean_returns, cov_matrix, risk_free_rate)

    max_sharpe_idx = np.argmax(results[2])
    sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]

    plt.figure(figsize=(10, 7))
    plt.scatter(results[0, :], results[1, :], c=results[2, :],
                cmap='YlGnBu', marker='o', s=10, alpha=0.3)
    plt.scatter(sdp, rp, marker='*', color='r',
                s=500, label='Maximum Sharpe ratio')
    plt.show()


quandl.ApiConfig.api_key = 'pLAzMCYGMdJF92iuN648'
data = quandl.get_table(
    'WIKI/PRICES',
    ticker=positions,
    qopts={'columns': ['date', 'ticker', 'adj_close']},
    date={'gte': '2016-1-1', 'lte': '2017-12-31'}, paginate=True)


df = data.set_index('date')
print(df)
table = df.pivot(columns='ticker')
print(table)
table.columns = [col[1] for col in table.columns]
returns = table.pct_change()
mean_returns = returns.mean()
cov_matrix = returns.cov()
num_portfolios = 25000
risk_free_rate = 0.0178

display_simulated_ef_with_random(
    mean_returns, cov_matrix, num_portfolios, risk_free_rate)
