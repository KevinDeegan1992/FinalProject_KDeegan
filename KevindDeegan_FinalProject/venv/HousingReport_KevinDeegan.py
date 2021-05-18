import pandas as pd
import numpy as np
import string
import os
import glob
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import zscore
from csv import reader

df = pd.read_csv('House_Prices.csv')

x = df['Date'].head(25)
y1 = df['Price'].head(25)
y2 = df['County'].head(25)

print(x)
print(y1)
print(y2)

print(df['Price'].value_counts())

group_county = df.groupby('County')
print(group_county.first())

print(group_county.get_group('Dublin'))

group_county_price = df.groupby(['County','Price'])
print(group_county_price.first())
print(group_county_price.last())

#Need to group by county then parse into the x plot varible
#Need to sort from low to high also

sorted_values = df.sort_values(by="Price",ascending=True)

price_data = df['Price']
county_data = df['County']
date_data = df['Date']

plt.plot(x,y1)
plt.show()

df['Date'] = pd.to_datetime(df.Date, infer_datetime_format = True)
print(df.head())

plt.plot(x,y1)
plt.show()

df.set_index('Date').groupby(pd.Grouper(freq='D')).mean()
print(df.tail())

plt.plot(y2,y1)
plt.show()

sns.lineplot(x = df['Price'].head(5), y = df['County'].head(5) )


#price_set = {'County':['Dublin','Cork','Galway','Kildare','Meath'], #example of how to plot a line graph from different regions using a
            #'Year':[2016,2017,2018,2019,2020],
            #'Price':[1000,2500,3500,5000,10000]}

#df = pd.DataFrame(data=price_set)

#print(df)

#county_set = set(df['County'])

#plt.figure()
#for county in county_set:
    #selected_data = df.loc[df['County'] == county]
    #plt.plot(selected_data['Year'], selected_data['Price'], label=county)

#plt.legend()
#plt.show()

#df['Price'].plot(kind='hist', bins=5)#histogram example
#plt.show()






