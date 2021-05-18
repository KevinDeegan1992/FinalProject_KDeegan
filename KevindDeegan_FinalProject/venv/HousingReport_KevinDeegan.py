import pandas as pd
import numpy as np
import string
import os
import glob
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

#df = pd.read_csv('House_Prices.csv')
#print(df['Price'].value_counts())

#group_county = df.groupby('County')
#print(group_county.first())

#print(group_county.get_group('Dublin'))

#group_county_price = df.groupby(['County','Price'])
#print(group_county_price.first())
#print(group_county_price.last())

#Need to group by county then parse into the x plot varible
#Need to sort from low to high also

#sorted_values = df.sort_values(by="Price",ascending=False)

#housing_subset = ["Date",
                  #"Price",
                  #"Address",
                  #"County",
                  #]

df = pd.read_csv('House_Prices.csv')
print(df.head())
print(df.describe())



