from datetime import datetime 
import os, sys
from logger import logging as lg
import numpy as np
import pandas as pd

class dataTransform:

    def __init__(self):
        self.logger = lg

    def read_data(self):
        try:
            lg.INFO("We are inside the data frame")
            df = pd.read_csv(r"/config/workspace/mushroom.csv")
            print(df)
        except Exception as e:
            print("Check the logs in case your code fails")
            lg.error("Error has occured")
            lg.Exception(str(e))
    
    def max_column(self):
        try:
            lg.INFO("We are expanding the column to see the complete column in the data frame")
            df = pd.set_option('display.max_columns', None)
            print(df)
        except Exception as e:
            print("Check the logs in case your code fails")
            lg.error("Error has occured")
            lg.Exception(str(e))

    def max_rows(self):
        try:
            lg.INFO("we are expanding the rows so that we can see the complete rows of the data frame")
            df = pd.set_option('dispaly.max_rows', None)
            print(df)
        except Exception as e:
                print('check the logs in case your code fails')
                lg.error('Error has occured')
                lg.Exception(str(e))
    
    def repalce_Question_marks_in_dataset(self):
        try:
            lg.INFO('we are counting the "?" marks in the stalk-root column')
            print(f"stalk root column contains {df['stalk-root'][df['stalk-root']=='?'].count()} question marks '?' hence {df['stalk-root'][df['stalk-root']=='?'].count()} missing values in this column")
            df['stalk-root'] = df['stalk-root'].replace('?', np.nan)
            print(f'checking total null values in each column {df.isna().sum()}')
        except Exception as e:
            print('check the log in case your code fails')
            lg.error('Error has occured')
            lg.Exception(str(e))
    
    def finding_number_of_unique_category_in_each_column(self):
        try:
            lg.INFO('we are finding the number of unique category in each column')
            for i in df.column:
                print(i, df[i].nunique())
        except Exception as e:
            print('check the logs in case your code fail')
            lg.error('Error has occured')
            lg.Exception(str(e))
    
    

