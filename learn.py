import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.pipeline.data_pipeline import DataPipeline
from src.components.model_trainer import ModelTrainer

def start_training():
    try:
        ingestion = DataIngestion()
        train_data, test_data = ingestion.initiate_data_ingestion()
        
        data_transformtion = DataTransformation()
        X_train, y_train = data_transformtion.initiate_data_transformation(train_data)
        
        pipeline_obj = DataPipeline()
        data_pipeline = pipeline_obj.create_pipeline()
        print(X_train.columns)
        X_train_trans = data_pipeline.fit_transform(X_train)

        trainer_obj = ModelTrainer()
        report = trainer_obj.get_model_score(X_train_trans, y_train)
        return report
    
    except Exception as e:
        print(e)
        logging.info(e)
        raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        logging.info("Training Started")
        print(start_training())
    except Exception as e:
        raise CustomException(e, sys)

