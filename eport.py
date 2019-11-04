import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = '3qNsf3VUNsvytS7sS_7W'
selected = ['TSLA', 'FB', 'BX', 'GE', 'AAPL']
data = quandl.get_table('WIKI/PRICES', ticker = selected, qopts = { 'columns': ['date', 'ticker', 'adj_close'] }, date = { 'gte': '2014-1-1', 'lte': '2016-12-31' }, paginate=True)

data.head()