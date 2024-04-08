import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from src.exception import CustomException
from src.logger import logging
import sys
from src.pipeline.prediction_pipeline import CustomData
from src.utils.artifacts_utils import load_object

app = Flask(__name__)

data_pipeline = load_object('data')
model = load_object()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    '''
    For rendering result on thr HTML GUI
    '''
    try:
        
        logging.info("Capturing the user inputs")

        custom_data =  CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))

        )
        
        features = custom_data.get_data_as_data_frame()
        trans_features = data_pipeline.transform(features)
        prediction = model.predict(trans_features)

        output = round(prediction[0], 2)

        return render_template('index.html', 
                            prediction_text = 'Predicted math score of the student is {}'.format(output))

    except Exception as e:
        raise CustomException(e, sys)

def predict_api():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")

