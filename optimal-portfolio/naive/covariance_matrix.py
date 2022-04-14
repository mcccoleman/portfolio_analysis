import pandas as pd
import matplotlib.pyplot as plt

MARKET_DAYS_PER_YEAR = 252
RISK_FREE_RATE = 0
NUM_OF_SIMULATIONS = 10000

data = pd.read_csv('./position_adjusted_close.csv', header= 0, index_col=False)
df = data.set_index('date')
positions = list(df.columns)
returns = df.pct_change()
mean_returns = returns.mean()
corr_matrix = returns.corr()

def runner():
    f = plt.figure(figsize=(6, 6))
    plt.matshow(corr_matrix, fignum=f.number)
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=45)
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16);
    plt.show()
    
runner()