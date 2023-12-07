import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

btc_data = yf.download('BTC-USD', start='2023-01-01', end='2023-12-31', progress=False)

btc_data['Daily_Returns'] = btc_data['Close'].pct_change()

btc_data['NUPL'] = (btc_data['Daily_Returns'] + 1).cumprod() - 1

cmap = plt.get_cmap('RdYlGn')  # Red-Yellow-Green color map
norm = plt.Normalize(btc_data['NUPL'].min(), btc_data['NUPL'].max())

# Plotting
fig, ax = plt.subplots()

colors = cmap(norm(btc_data['NUPL']))

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, label='NUPL')

btc_dates = np.linspace(0, 1, len(btc_data))  # Normalize x-axis for heatmap
btc_prices = btc_data['Close']
ax.scatter(btc_dates, btc_prices, c=colors, cmap=cmap)

# Display the plot
plt.title('BTC Price Heatmap with NUPL Grading')
plt.xlabel('Date')
plt.ylabel('BTC Price')
plt.show()
