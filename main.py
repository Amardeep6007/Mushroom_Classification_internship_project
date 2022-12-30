from log import logging as lg
from DataTransform.data_transform import dataTransform
from Encoding.encoder import encoder

#obj_data_transform = dataTransform()
#obj_data_transform.data_cleaning_and_extract_balanced_Dataset()

obj_encoder = encoder()
obj_encoder.Encoded_Dataframe()