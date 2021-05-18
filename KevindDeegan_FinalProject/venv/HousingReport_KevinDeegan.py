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
print(df['Price'].value_counts())

group_county = df.groupby('County')
print(group_county.first())

print(group_county.get_group('Dublin'))

group_county_price = df.groupby(['County','Price'])
print(group_county_price.first())
print(group_county_price.last())

#Need to group by county, parse into the x plot varible
#Need to sort from low to high also
#For the purposes of this analysis, I will use top 5 counties: Dublin, Cork, Galway, Kildare, Meath. For ease the cutoff point is 18000 housing units
#Need to convert Price to float

sorted_values = df.sort_values(by='Price',ascending=False)
cutoff_point = str(500000000)

top_counties = ['Date','County','Price']#list without addresses
top_county_list = pd.read_csv('House_Prices.csv', names=top_counties)
























