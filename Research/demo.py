import pandas as pd
import numpy as np
data = pd.read_csv('./DataSets/princekd26805_17703994220842927.csv')
# print(data.isna().sum())
data.drop('Minimum Faecal Streptococci Required For River Water (UOM:MPN/100ML(MostprobableNumberper100mililiters)), Scaling Factor:1', axis=1, inplace=True)
# # print(data.isna().sum())
data.drop('Maximum Faecal Streptococci Required For River Water (UOM:MPN/100ML(MostprobableNumberper100mililiters)), Scaling Factor:1', axis=1, inplace=True)

print(data.isna().sum())

df = data.fillna(data.mean(numeric_only=True))
print(df.isna().sum())

# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())
# print(df.columns)
