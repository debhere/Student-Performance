import sys
import yaml
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils.artifacts_utils import PipelineArtifactConfig

from functools import reduce

from dataclasses import dataclass

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

from sklearn.linear_model import LinearRegression, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import r2_score

@dataclass
class BaseModel:
    model_repo =  {
            'RandomForestRegressor': RandomForestRegressor(),
            'LinearRegression': LinearRegression(),
            'Lasso': Lasso(),
            'ElasticNet': ElasticNet(),
            'DecisionTreeRegressor': DecisionTreeRegressor(),
            'GradientBoostingRegressor': GradientBoostingRegressor()
        }


class ModelTrainer:
    def __init__(self):
        self.models = BaseModel()

    def get_base_model_score(self, X, y, scoring="r2"):
        try:
            score_map = {}
            logging.info("Training in progress...")
            for name, model in self.models.model_repo.items():
                cv_scores = cross_val_score(model, X, y, cv=5, scoring=scoring)
                score_map[name] = np.mean(cv_scores)

            logging.info("Base model training is completed")
            return score_map
    
        except Exception as e:
            logging.info(e)
            raise CustomException(e, sys)
        
    def evaluate_base_model_on_test(self, X_train, y_train, X_test, y_test):
        try:
            test_score_map = {}
            logging.info("Evaluation in progress")

            for name, model in self.models.model_repo.items():
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                score = r2_score(y_test, y_pred)
                test_score_map[name] = score

            logging.info("Test Evaluation is completed")
            return test_score_map
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def model_tuning(self, X, y):
        logging.info("Hyper-Parameter tuning in progress")
        estimator_list = {}
        with open("model.yaml") as f:
            try:
                model_params = yaml.safe_load(f)

                for model, params in model_params.items():
                    scv = GridSearchCV(self.models.model_repo[model], params, cv=5, scoring='r2')
                    scv.fit(X, y)
                    estimator_list[round(scv.best_score_, 4)] = scv.best_estimator_

                #best_model, 
                best_score = np.max(list(estimator_list.keys()))

                pipe = PipelineArtifactConfig()
                pipe.save_model_pipeline("best_estimator.pkl", estimator_list[best_score])
                return estimator_list[best_score]
                
            except Exception as e:
                raise CustomException(e, sys)
