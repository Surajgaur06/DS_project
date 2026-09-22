import pandas as pd
df = pd.read_csv('Iris.csv')
print(df)

df = pd.read_csv('Iris.csv', index_col=0)
print(df)

