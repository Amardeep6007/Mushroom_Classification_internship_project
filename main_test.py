import pandas as pd 

df_2 = pd.read_csv('/config/workspace/cleaned_nd_Encoded_mushroom.csv')
#print(df_2.drop(['Unnamed: 0.1','Unnamed: 0'],axis=1, inplace= True))
#print(df_2.head())
#print(df_2.isna().sum())
print(df_2.columns)
