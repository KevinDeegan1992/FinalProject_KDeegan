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

x = []
y = []

with open('House_Prices.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append(row[0])
        y.append(row[1])

        plt.bar(x, y, color='g', width=0.72, label="Price of Houses")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('House Prices')
        plt.legend()
        plt.show()

