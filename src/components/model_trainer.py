import sys
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

@dataclass
class BaseModel:
    model_repo =  {
            'RandomForestRegressor': RandomForestRegressor(),
            'LinearRegression': LinearRegression(),
            'DecisionTreeRegressor': DecisionTreeRegressor()
        }


class ModelTrainer:
    def __init__(self):
        self.models = BaseModel()

    def _trainer_fit(self, X, y):
        try:
            for name, estimator in self.models.model_repo.items():
                estimator.fit(X, y)
        except:
            pass

    def get_model_score(self, X, y, scoring="r2"):
        try:
            score_map = {}
            logging.info("Training in progress...")
            for name, model in self.models.model_repo.items():
                cv_scores = cross_val_score(model, X, y, cv=5, scoring=scoring)
                score_map[name] = np.mean(cv_scores)

            return score_map
        except Exception as e:
            logging.info(e)
            raise CustomException(e, sys)
