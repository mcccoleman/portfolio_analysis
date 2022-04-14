import pandas as pd
import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
import itertools

MARKET_DAYS_PER_YEAR = 252
RISK_FREE_RATE = 0
NUM_OF_SIMULATIONS = 10000

data = pd.read_csv('./position_adjusted_close.csv', header= 0, index_col=False)
df = data.set_index('date')
positions = list(df.columns)
returns = df.pct_change()
mean_returns = returns.mean()
cov_matrix = returns.cov()

def get_sharpe_ratio_for_portfolio(portfolio_return, risk_free_rate, portfolio_std_dev):
    return (portfolio_return - risk_free_rate) / portfolio_std_dev

def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights) * MARKET_DAYS_PER_YEAR
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(MARKET_DAYS_PER_YEAR)
    return std, returns
    
    
def generate_random_portfolio_weights(mean_returns):
    weights = np.random.random(len(mean_returns))
    weights /= np.sum(weights)
    return weights


def generate_random_portfolio_weights_and_results(mean_returns, cov_matrix, risk_free_rate, num_portfolios):
    results = np.zeros((3, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = generate_random_portfolio_weights(mean_returns)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = get_sharpe_ratio_for_portfolio(portfolio_return, risk_free_rate, portfolio_std_dev)
    return results, weights_record

def get_index_of_max_sharpe_ratio(results):
    return np.argmax(results[2])

def display_simulated_ef(results):
    max_sharpe_idx = get_index_of_max_sharpe_ratio(results)
    plt.figure(figsize=(10, 7))
    plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='YlGnBu', marker='o', s=10, alpha=0.3)
    sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]
    plt.scatter(sdp, rp, marker='*', color='b', s=500, label='Maximum Sharpe ratio')
    plt.show()

def get_optimal_weights_for_positions(results, weights):
    max_sharpe_idx = get_index_of_max_sharpe_ratio(results)
    optimal_weight = np.array(weights[max_sharpe_idx])
    included_positions = np.array(positions)
    optimal_weight_dataset = pd.DataFrame({'positions': included_positions, 'weights': optimal_weight}, columns=['positions', 'weights'])
    return optimal_weight_dataset

def run_simulations():
    results, weights = generate_random_portfolio_weights_and_results(mean_returns, cov_matrix, RISK_FREE_RATE, NUM_OF_SIMULATIONS)
    display_simulated_ef(results)
    print(get_optimal_weights_for_positions(results, weights)) 
    
def test():
    print(itertools.combinations(range(4), 10))
    
run_simulations()
