import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.utils.artifacts_utils import DataArtifactConfig


# @dataclass
# class DataIngestionConfig:
#     train_data_path:str = os.path.join("artifacts", "train.csv")
#     test_data_path:str = os.path.join("artifacts", "test.csv")
#     raw_data_path:str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        #self.ingestion_config = DataIngestionConfig()
        self.utils = DataArtifactConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered into the data ingestion component")
        try:
            source_data_path = self.utils.get_data_artifact_path(filetype="source")
            #df = pd.read_csv("Data\StudentsPerformance.csv")
            df = pd.read_csv(source_data_path)
            logging.info("Read dataset as dataframe")

            raw_data_path = self.utils.get_data_artifact_path(filetype="raw", filename="raw.csv")
            train_data_path = self.utils.get_data_artifact_path(filetype="train", filename="train.csv")
            test_data_path = self.utils.get_data_artifact_path(filetype="test", filename="test.csv")

            #os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            df.to_csv(raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            #train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            #test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            train_set.to_csv(train_data_path, index=False, header=True)
            test_set.to_csv(test_data_path, index=False, header=True)

            logging.info("Data ingestion is completed")

            return (
                train_data_path,
                test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)