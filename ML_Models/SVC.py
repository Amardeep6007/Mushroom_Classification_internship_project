import pandas as pd 
from sklearn.preprocessing import LabelEncoder
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
from sklearn.decomposition import PCA
import logging as lg 

class support_vector_classifier_class:
    def __init__(self):
        self.logger = lg

    def svc_method(self):
        try:
            lg.info('we are inside the Support Vector classifier model')
            df = pd.read_csv(r'/config/workspace/cleaned_nd_Encoded_mushroom.csv')
            x= df.drop('class', axis= 1)
            y= df['class']

            pca1 = PCA(n_components=7)
            pca_fit = pca1.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(pca_fit, y, test_size = 0.20, random_state = 42)

            svc_obj = SVC()
            svc_obj.fit(x_train, y_train)
            y_predict3 = svc_obj.predict(x_test)

            print("Accuracy of Support Vector Classifier Model", accuracy_score(y_test, y_predict3))

            svc_model = SVC()
            svc_model.fit(pca_fit, y)
            filename = r'/config/workspace/Model_saved/svc_Pickle.pkl'
            pickle.dump(svc_model, open(filename, 'wb'))
            

        except Exception as e:
            print('Check log in case your code fails')
            lg.error("Error has occured")
            lg.exception(str(e))