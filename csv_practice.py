import pandas as pd
import numpy as np

headers_data = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv('C:/Users/USER 16/Downloads/dataset_1.data', names = headers_data)
print(df)
print(df.head(10))
print(df.tail(12))
print(df.dtypes)
print(df.describe(include = 'all'))
df.to_csv('automobile.csv', index = False)