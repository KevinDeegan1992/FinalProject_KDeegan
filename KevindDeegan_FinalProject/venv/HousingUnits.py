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
print(df.describe())

df['County'].value_counts().plot(kind='bar')
plt.title('Number of Houses') #Simple way of visualising the amount of houses across the country of Ireland, with Dublin reaching over 140000 houses
plt.xlabel('County')
plt.ylabel('Housing Units')
plt.show()
