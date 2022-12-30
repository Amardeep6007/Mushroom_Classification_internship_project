from log import logging as lg
from DataTransform import data_transform

if __name__=='__main__':
    try:
        obj_data_transform = data_transform()
        print(obj_data_transform)
    except Exception as e:
        print('check log in case your code doesnt work')
