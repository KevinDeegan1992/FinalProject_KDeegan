import pandas as pd
import numpy as np

#Read Netflix CSV
netflix_data = pd.read_csv("netflix_titles.csv")

missing_values_count = netflix_data.isnull().sum()
print(missing_values_count)

print(netflix_data.head())
print(missing_values_count[0:])

droprows = netflix_data.dropna()
print(netflix_data.shape,droprows.shape)

cleaned_data = netflix_data.fillna(0)
print(cleaned_data)

drop_duplicates = netflix_data.drop_duplicates()
print(netflix_data.shape)