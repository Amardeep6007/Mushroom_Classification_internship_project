import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle
from sklearn.decomposition import PCA
import logging as lg 

class GradientBoostingclass:
    def __init__(self):
        self.logger = lg

    def Gradient_Boosting_Classifier(self):
        try:
            lg.info('we are inside the Gradient Boosting Classifier')
            df = pd.read_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
            x= df.drop('class', axis= 1)
            y= df['class']

            pca1 = PCA(n_components=7)
            pca_fit = pca.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(pca_fit, y, test_size = 0.20, random_state = 42)

            gbc = GradientBoostingClassifier()
            gbc.fit(x_train, y_train)
            y_predict6 = gbc.predict(x_test)

            print("Accuracy of Gradient Boosting Classifier ", accuracy_score(y_test, y_predict6))

            gbc_model = GradientBoostingClassifier()
            gbc_model.fit(pca_fit, y)
            filename = r'/config/workspace/Model_saved/gradient_boosting_Pickle.pkl'
            pickle.dump(gbc_model, open(filename, 'wb'))

        except Exception as e:
            print('Check log in case your code fails')
            lg.error("Error has occured")
            lg.Exception(str(e))