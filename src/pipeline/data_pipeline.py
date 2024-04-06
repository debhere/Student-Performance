import sys
from src.exception import CustomException
from src.logger import logging
from src.utils.artifacts_utils import ArtifactConfig

from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer



class DataPipeline:
    def __init__(self):
        logging.info("Creating data pipeline")
        self.utils = ArtifactConfig()
        self.data_trans = DataTransformation()
        self.ingestion = DataIngestion()

    
    def create_pipeline(self, X):

        try:
            num_cols, cat_cols = self.data_trans.get_data_transformer_object()

            num_pipeline = Pipeline(
                [
                    ('imputer', SimpleImputer()),
                    ('scaler', StandardScaler())

                ]
            )
            cat_pipeline = Pipeline(
                [
                    ('imputer', SimpleImputer(strategy="most_frequent")),
                    ('scale', StandardScaler())

            ])

            data_trans_pipeline = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, num_cols),
                    ('cat_pipeline', cat_pipeline, cat_cols)
                
            ])

            pipeline_path = self.utils.save_object_artifact("data_pipeline.pkl")
            return data_trans_pipeline
        
        except Exception as e:
            raise Exception(e, sys)
        

class ModelPipeline:
    pass