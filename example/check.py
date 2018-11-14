import pandas as pd

df = pd.read_csv("result.csv")
df.sort_values(by=["Script_result", "AvgTime"], ascending=[False, True], inplace=True)
df['Index'] = range(1, len(df)+1)
df = df.set_index('Index')
df.to_csv("1.csv")
print(df)