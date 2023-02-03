import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Make a request to the website
URL = "https://finance.yahoo.com/quote/SPY/history?p=SPY"
page = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Extract the data from the table
data = []
for row in soup.find_all("tr"):
    cells = row.find_all("td")
    if cells:
        data.append(cell.text for cell in cells)

# Create the Pandas dataframe and set the column names
df = pd.DataFrame(data)
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Change', 'Volume']

# Convert the date column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the RSI using the close prices
rsi = ta.rsi(df['Close'], timeperiod=14)

# Add the RSI as a new column in the dataframe
df['RSI'] = rsi

# Create the plot
fig, ax1 = plt.subplots()
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price')
ax1.plot(df['Date'], df['Close'], color='blue')
ax2 = ax1.twinx()
ax2.set_ylabel('RSI')
ax2.plot(df['Date'], df['RSI'], color='red')
plt.show()

print(df)