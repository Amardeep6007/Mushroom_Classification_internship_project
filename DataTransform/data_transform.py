from datetime import datetime 
import os, sys
from logger import logging 
import numpy as np
import pandas as pd

class dataTransform:

    def __init__(self):
        self.logger = logging

    def read_data(self):
        try:
            df = pd.read_csv(r"/config/workspace/mushroom.csv")
            print(df)
        except Exception as e:
            print("Check the logs in case your code fails")
            logging.error("Error has occured")
            logging.Exception(str(e))
            

