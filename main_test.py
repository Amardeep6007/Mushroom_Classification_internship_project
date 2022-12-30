import pandas as pd 

df_2 = pd.read_csv('/config/workspace/cleaned_mushroom.csv')
print(df_2.isna().sum())