import sys
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException




if __name__ == "__main__":
    try:
        logging.info("Training Started....!!!")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        print(train_data_path, test_data_path)
    except Exception as e:
        raise CustomException(e, sys)