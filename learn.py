import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.pipeline.data_pipeline import DataPipeline
from src.components.model_trainer import ModelTrainer
from src.utils.artifacts_utils import PipelineArtifactConfig

from sklearn.metrics import r2_score

def start_training():
    try:
        logging.info("Starting data imgestion...!!!")
        ingestion = DataIngestion()
        train_data, test_data = ingestion.initiate_data_ingestion()
        
        logging.info("Starting data transformation...!!!")
        data_transformtion = DataTransformation()
        X_train, y_train = data_transformtion.initiate_data_transformation(train_data)
        
        logging.info("Starting data pipeline creation...!!!")
        pipeline_obj = DataPipeline()
        data_pipeline = pipeline_obj.create_pipeline(X_train)
        X_train_trans = data_pipeline.transform(X_train)

        logging.info("Starting base model scoring...!!!")
        trainer_obj = ModelTrainer()
        base_model_score = trainer_obj.get_base_model_score(X_train_trans, y_train)
        
        logging.info("Starting model evauation on test data...!!!")
        X_test, y_test = data_transformtion.initiate_data_transformation(test_data)
        X_test_trans = data_pipeline.fit_transform(X_test)
        test_pred_score = trainer_obj.evaluate_base_model_on_test(X_train_trans, y_train, X_test_trans, y_test)

        best_train_model, best_train_score = trainer_obj.model_tuning(X_train_trans, y_train)

        # best_test_model, best_test_score = trainer_obj.model_tuning(X_test_trans, y_test)

        y_pred = best_train_model.predict(X_test_trans)
        score_test = r2_score(y_test, y_pred)

        print(score_test)

        return base_model_score, test_pred_score, best_train_model, best_train_score
    
    except Exception as e:
        print(e)
        logging.info(e)
        raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        logging.info("Training Started")
        base_model_score, test_pred_score, best_train_model, best_train_score = start_training()
        logging.info("Training and evaluation completed for base models")
        print(base_model_score)
        print(test_pred_score)
        print(best_train_model)
        print(best_train_score)
        pipe = PipelineArtifactConfig()
        print(pipe.get_data_pipeline())
        # print(best_test_model)
        # print(best_test_score)


    except Exception as e:
        raise CustomException(e, sys)

