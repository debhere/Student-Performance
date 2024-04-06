import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
from src.logger import logging
#from src.utils.artifacts_utils import ArtifactConfig


# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        logging.info("Data transformation process initialized")
        #self.data_transformation_config = DataTransformationConfig()
        #self.utils = ArtifactConfig()

    def get_column_info(self):
        '''
        This function is responsible for our data transformation
        '''

        try:
            num_cols = ["writing score", 'reading score']
            cat_cols = ['gender', 'race/ethnicity', 'parental level of education', 'lunch',
                        'test preparation course']
            
            # num_pipeline = Pipeline(
            #     [('imputer', SimpleImputer(strategy="median")),
            #      ('scaler', StandardScaler())]
            # )

            # logging.info("Numerical columns transformation completed")

            # logging.info(f"Numerical Columns: {num_cols}")
            # logging.info(f"Categorical Columns: {cat_cols}")

            # cat_pipeline = Pipeline(

            #     [('imputer', SimpleImputer(strategy="most_frequent")),
            #      ('one_hot', OneHotEncoder()),
            #      ('scaler', StandardScaler())]
            # )

            # logging.info("Catgorical columnns transformation completed")

            # preprocessor = ColumnTransformer(
            #     [('num_pipeline', num_pipeline, num_cols),
            #      ('cat_pipeline', cat_pipeline, cat_cols)
            #      ]
            # )

            # logging.info("Column Tranformation is completed")

            return num_cols, cat_cols



        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, data_path):
        try:
            
            # train_df = pd.read_csv(train_path)
            # test_df = pd.read_csv(test_path)

            data_df = pd.read_csv(data_path)

            logging.info("Reading training & test data")

            logging.info("Obtaining preproccessing object")

            #preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "math score"
            #num_cols = ["writing score", 'reading score']

            X = data_df.drop(columns=target_column_name, axis=1)
            y = data_df[target_column_name]
            #input_feature_train_df = train_df.drop(columns = target_column_name, axis=1)
            #target_feature_train_df = train_df[target_column_name]

            # input_feature_test_df = test_df.drop(columns = target_column_name, axis=1)
            # target_feature_test_df = test_df[target_column_name]

            return X, y

        except Exception as e:
            raise CustomException(e, sys)