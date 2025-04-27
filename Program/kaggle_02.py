import pandas as pd

df = pd.read_csv("../Datasets/train.csv")
print(df.describe())
print(df.isnull().sum())