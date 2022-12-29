from sklearn.preprocessing import LabelEncoder
import pandas as pd 
from logger import logging as lg
import os, sys
import csv

class encoder:
    def __init__(self):
        self.logging = lg
    
    def Encoded_Dataframe(self):
        try:
            le = LabelEncoder()
            df = pd.read_csv(r'/config/workspace/cleaned_mushroom.csv')
            for i in df.column:
                df[i] = le.fit_transform(df[i])

                df1= df.to_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
                prin(df1)
        except Exception as e:
            lg.Exception(e)
            return e

#calling the encoder class
#obj.encoder()
#obj.Encoded_Dataframe()