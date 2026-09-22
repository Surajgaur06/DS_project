import seaborn as sns
df = sns.load_dataset("titanic")
print("data shape:", df.shape)
print(df.head())