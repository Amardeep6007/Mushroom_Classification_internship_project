from datetime import datetime 
import os, sys
from logger import logging as lg
import numpy as np
import pandas as pd
from sklearn_pandas import SingleImputer
from sklearn_pandas import CategoricalImputer
from autoimpute.imputations import SingleImputer,MultipleImputer
from autoimpute.imputations.series import MultinomialLogisticImputer
from sklearn.preprocessing import LabelEncoder


class dataTransform:

    def __init__(self):
        self.logger = lg

    def data_cleaning_and_extract_balanced_Dataset(self):
        try:
            lg.info('we are inside the data frame')
            df = pd.read_csv(r'/config/workspace/mushroom.csv') #read the csv file and store in the dataframe
            
            lg.info('setting the max column of the data frame')
            pd.set_option('display.max_columns', None) #setting the data frame to view all the columns of the data frame
            
            lg.info('printin the top 5 records of the data set')
            print(df.head()) #printing the first 5 records of the data frame initially
            
            lg.info(r'counting the "?" marks in the stalk-root column')
            print(f"stalk root column contains {df['stalk-root'][df['stalk-root']=='?'].count()} question marks '?' hence {df['stalk-root'][df['stalk-root']=='?'].count()} missing values in this column") #printing the number of question marks in the stalk root column
            
            lg.info(r'replacing the "?" marks with null values')
            df['stalk-root'] = df['stalk-root'].replace('?',np.nan) # replace the '?' marks with null values 
            
            lg.info(r'count the null values in each column of the data frame')
            print(df.isna().sum()) # counting the null values in each columns
            
            lg.info(r'dropping the veil-type column')
            df = df.drop(['veil-type'], axis=1) #dropping the veil-type column because it has only 1 category mentioned which does not provide any insight
            
            lg.info(r'inputing the null values in the data frame')
            impute =SingleImputer(strategy= 'categorical') #creating object of SingleImputer class
            impute.fit(df) #fitting the data frame to impute the null values in the data frame
            new_df =impute.transform(df) #transforming the data frame to impute the null values in the data frame
            
            lg.info(r'exporting the cleaned data frame')
            new_df = pd.to_csv(r'/config/workspace/cleaned_mushroom.csv') #exporting the cleaned csv
            print((new_df))
        except Exception as e:
            print('check the log file incase your code fails')
            lg.Exception(str(e))
            lg.error('errotr has occured')
