from log import logging as lg
from DataTransform.data_transform import dataTransform
from Encoding.encoder import encoder
from ML_Models.DecisionTreeClassifier import DecisionTreeClassifierclass
from ML_Models.GradientBoosting import GradientBoostingclass
from ML_Models.LogisticRegression import LogisticRegressionclass
from ML_Models.RandomForest import random_forest_class
from ML_Models.SVC import support_vector_classifier_class

obj_data_transform = dataTransform()
obj_data_transform.data_cleaning_and_extract_balanced_Dataset()

obj_encoder = encoder()
obj_encoder.Encoded_Dataframe()

obj_DecisionTreeClassifierclass = DecisionTreeClassifierclass()
obj_DecisionTreeClassifierclass.Decision_tree_Classifier_method()

obj_GradientBoostingclass = GradientBoostingclass()
obj_GradientBoostingclass.Gradient_Boosting_Classifier_method()

obj_LogisticRegressionclass = LogisticRegressionclass()
obj_LogisticRegressionclass.lr_method()

obj_random_forest_class = random_forest_class()
obj_random_forest_class.rf_method()

obj_support_vector_classifier_class = support_vector_classifier_class()
obj_support_vector_classifier_class.svc_method()

