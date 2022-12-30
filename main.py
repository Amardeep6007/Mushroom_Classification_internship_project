import pandas as pd 
from log_folder.log import logging as lg

lg.info('we are inside the data frame and it is read successfully')
df = pd.read_csv('/config/workspace/mushrooms.csv')
print(df.head())