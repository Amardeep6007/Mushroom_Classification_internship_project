from datetime import datetime 
import os, sys
from logger import logging as lg
import numpy as np
import pandas as pd

class dataTransform:

    def __init__(self):
        self.logger = lg

    def data_cleaning_and_extract_balanced_Dataset(self):
        try:
            lg.info('we are inside the data frame')
            df = pd.read_csv(r'/config/workspace/mushroom.csv') #read the csv file and store in the dataframe
            pd.set_option('display.max_columns', None) #setting the data frame to view all the columns of the data frame
            print(df.head()) #printing the first 5 records of the data frame initially
            print(f"stalk root column contains {df['stalk-root'][df['stalk-root']=='?'].count()} question marks '?' hence {df['stalk-root'][df['stalk-root']=='?'].count()} missing values in this column") #printing the number of question marks in the stalk root column
            df['stalk-root'] = df['stalk-root'].replace('?',np.nan) # replace the '?' marks with null values 
            print(df.isna().sum()) # counting the null values in each columns
            df = df.drop(['veil-type'], axis=1) #dropping the veil-type column because it has only 1 category mentioned which does not provide any insight
            



            

