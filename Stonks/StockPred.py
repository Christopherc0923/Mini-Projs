import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

spy = yf.Ticker("SPY")
history = spy.history(period = "max")
print(history.head())