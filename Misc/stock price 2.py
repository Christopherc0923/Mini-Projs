import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

spy = yf.Ticker('SPY')
df = spy.history()
df = df.reset_index()
print(df.columns)
print(df.head())


df['Date'] = pd.to_datetime(df['Date'])

# Calculate the RSI using the close prices over a period of 365 days
rsi = ta.rsi(df['Close'], timeperiod = 365)

# Add the RSI as a new column in the dataframe
df['RSI'] = rsi
print(df.head())
# Create the plot
fig, ax1 = plt.subplots()
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price')
ax1.plot(df['Date'], df['Close'], color='blue')
ax2 = ax1.twinx()
ax2.set_ylabel('RSI')
ax2.plot(df['Date'], df['RSI'], color='red')
plt.show()