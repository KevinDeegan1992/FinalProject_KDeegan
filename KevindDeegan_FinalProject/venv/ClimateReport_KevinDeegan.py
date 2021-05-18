import pandas as pd
import numpy as np
import os
import glob
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

df = pd.read_csv('Climate_COVID.csv')

df = df.round(3)

