import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from sklearn.decomposition import PCA
import logging as lg 

class random_forest_class:
    def __init__(self):
        self.logger = lg

    def rf_method(self):
        try:
            lg.info('we are inside the Random Forest model')
            df = pd.read_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
            x= df.drop('class', axis= 1)
            y= df['class']

            pca1 = PCA(n_components=7)
            pca_fit = pca1.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(pca_fit, y, test_size = 0.20, random_state = 42)

            rm = RandomForestClassifier()
            rm.fit(x_train, y_train)
            y_predict5 = rm.predict(x_test)

            print("Accuracy of Ramdom Forest Model", accuracy_score(y_test, y_predict5))

            rf_model = RandomForestClassifier()
            rf_model.fit(pca_fit, y)
            filename = r'/config/workspace/Model_saved/random_forest_Pickle.pkl'
            pickle.dump(rf_model, open(filename, 'wb'))
            

        except Exception as e:
            print('Check log in case your code fails')
            lg.error("Error has occured")
            lg.exception(str(e))