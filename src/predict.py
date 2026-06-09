import joblib
import pandas as pd

from src.build_features import build_prediction_feature

class SalaryPredictor:
    def __init__(self):
        self.model=joblib.load("models/model.pkl")
        self.encoder=joblib.load("models/encoder.pkl")
        self.text_extractor=joblib.load("models/tfidf.pkl")
    def predict(self,job_data:dict):
        df=pd.DataFrame([job_data])
        X=build_prediction_feature(df,self.encoder,self.text_extractor)
        prediction=self.model.predict(X)
        return float(prediction[0])
    