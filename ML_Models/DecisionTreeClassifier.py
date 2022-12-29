import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle
from sklearn.decomposition import PCA
import logging as lg 

class DecisionTreeClassifier:
    def __init__(self):
        self.logger = lg

    def Decision_tree_Classifier(self):
        try:
            lg.info('we are inside the decision tree classifier')
            df = pd.read_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
            x= df.drop('class', axis= 1)
            y= df['class']

            pca1 = PCA(n_components=7)
            pca_fit = pca.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(pca_fit, y, test_size = 0.20, random_state = 42)

            dt = DecisionTreeClassifier()
            dt.fit(x_train, y_train)
            y_predict4 = dt.predict(x_test)

            print("Accuracy of Decision Tree Classifier ", accuracy_score(y_test, y_predict4))

            dt_model = DecisionTreeClassifier()
            dt_model.fit(pca_fit, y)
            filename = r'/config/workspace/Model_saved/decision_tree_Pickle.pkl'
            pickle.dump(dt_model, open(filename, 'wb'))

        except Exception as e:
            print('Check log in case your code fails')
            lg.error("Error has occured")
            lg.Exception(str(e))