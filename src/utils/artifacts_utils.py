import configparser
import os
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import sys
import joblib

@dataclass
class BaseConfigLoader:
    '''
    This is the base config loader class
    '''
    try:
        logging.info("Loading the base config")
        config = configparser.ConfigParser()
        config.read("config.ini")
        source_data_folder = config.get("Base Config", "source_data_folder")
        source_data_file = config.get("Base Config", "source_data_file")

        artifacts_base_folder = config.get("Base Config", "artifacts_base_folder")

        data_artifacts_folder = config.get("Base Config", "data_artifacts_folder")
        model_artifacts_folder = config.get("Base Config", "model_artifacts_folder")
        pipeline_artifacts_folder = config.get("Base Config", "pipeline_artifacts_folder")

        #data_pipeline_pickle = config.get("Base Config", "data_pipeline_pickle")
        #model_pickle = config.get("Base Config", "model_pickle")


    except Exception as e:
        raise CustomException(e, sys)


def create_path(root_folder, main_folder, filename):
    '''
    Creating the folder structure as applicable
    '''
    try:
        logging.info("Folder structure being initialized")
            
        folder_path = os.path.join(root_folder, main_folder)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, filename)

        return file_path
    
    except Exception as e:
        raise CustomException(e, sys)



class DataArtifactConfig:
    def __init__(self):
        self.base_config = BaseConfigLoader()

    # def _initiate_path(self, root_folder, main_folder, filename):
    #     '''
    #     Creating the folder structure as applicable
    #     '''
    #     try:
    #         logging.info("Folder structure being initialized")
            
    #         folder_path = os.path.join(root_folder, main_folder)
    #         os.makedirs(folder_path, exist_ok=True)

    #         file_path = os.path.join(folder_path, filename)

    #         return file_path
        
    #     except Exception as e:
    #         raise CustomException(e, sys)

    def get_data_artifact_path(self, filetype:str, filename=None) -> str:
        '''
        This util method returns the dedicated path for the raw data or the dedicated 
        path for the artifacts

        filetype = ['source','raw', 'train', 'test']

        '''

        file_path = ""

        try:
            if filetype == "source":
                source_data_path = os.path.join(self.base_config.source_data_folder, 
                                             self.base_config.source_data_file)
                
                file_path = source_data_path
                logging.info("Real data being fetched")
                
            elif filetype == "train" or filetype == "test" or filetype == "raw":
                train_test_data_path = create_path(self.base_config.artifacts_base_folder,
                                                      self.base_config.data_artifacts_folder, 
                                                      f"{filetype}.csv")
                

                file_path = train_test_data_path
                logging.info(f"Getting the folder path to store {filetype} data")

            else:
                logging.info("Invalid filetype given, please refer the DOCSTRING")


        
            return file_path if file_path is not None else exit()
                
        
        except Exception as e:
            raise CustomException(e, sys)
        


class PipelineArtifactConfig:
    def __init__(self):
        self.base_config = BaseConfigLoader()
        self.data_pipeline = None
        self.model_pipeline = None

    def save_data_pipeline(self, filename, pipeline_obj):
        root_folder = self.base_config.artifacts_base_folder
        data_pipeline_folder = self.base_config.pipeline_artifacts_folder
        self.data_pipeline = create_path(root_folder=root_folder, main_folder=data_pipeline_folder, filename=filename)
        joblib.dump(pipeline_obj, self.data_pipeline)

    def get_data_pipeline(self):
        return self.data_pipeline
    
    def save_model_pipeline(self, filename, model_obj):
        root_folder = self.base_config.artifacts_base_folder
        model_pipeline_folder = self.base_config.pipeline_artifacts_folder
        self.model_pipeline = create_path(root_folder=root_folder, main_folder=model_pipeline_folder, filename=filename)
        joblib.dump(model_obj, self.model_pipeline)
    
    def get_model_pipeline(self):
        return self.model_pipeline
    




