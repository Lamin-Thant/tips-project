import pandas as pd

df = pd.read_csv("tips.csv")

print("First 10 rows of tips.csv:")
print(df.head(10))
