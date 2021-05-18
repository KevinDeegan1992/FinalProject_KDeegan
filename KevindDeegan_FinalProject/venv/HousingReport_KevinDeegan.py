import pandas as pd
import numpy as np
import string
import os
import glob
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

df = pd.read_csv('House_Prices.csv')
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())

print(df['Price'].value_counts())

group_county = df.groupby('County')
print(group_county.first())

print(group_county.get_group('Dublin'))

group_county_price = df.groupby(['County','Price'])
print(group_county_price.first())
print(group_county_price.last())

