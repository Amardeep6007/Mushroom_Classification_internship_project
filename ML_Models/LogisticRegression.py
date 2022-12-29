import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
from sklearn.decomposition import PCA
import logging as lg 

class LogisticRegressionclass:
    def __init__(self):
        self.logger = lg

    def lr(self):
        try:
            lg.info('we are inside the Logistic Regression model')
            df = pd.read_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
            x= df.drop('class', axis= 1)
            y= df['class']

            pca1 = PCA(n_components=7)
            pca_fit = pca.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(pca_fit, y, test_size = 0.20, random_state = 42)

            lr = LogisticRegression()
            lr.fit(x_train, y_train)
            y_predict1 = lr.predict(x_test)

            print("Accuracy of Logistic Regression ", accuracy_score(y_test, y_predict1))

            lr_model = LogisticRegression()
            lr_model.fit(pca_fit, y)
            filename = r'/config/workspace/Model_saved/logistic_regression_Pickle.pkl'
            pickle.dump(lr_model, open(filename, 'wb'))
            

        except Exception as e:
            print('Check log in case your code fails')
            lg.error("Error has occured")
            lg.Exception(str(e))