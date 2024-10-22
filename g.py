import pandas as pd

path = "C:/Users/USER 16/Documents/machine-readable-business-employment-data-Jun-2024-quarter.csv"
data = pd.read_csv(path)

print(data.iloc[:, :2])