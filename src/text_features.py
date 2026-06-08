from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class TextFeatureExtractor:
    def __init__(self,max_features=100):
        self.vectorizer=TfidfVectorizer(
            max_features=max_features,
            stop_words="english"
        )
    def fi(self,df: pd.DataFrame):
        self.vectorizer.fit(df["Job Description"])
        return self
    def transform(self,df: pd.DataFrame):
        return self.vectorizer.transform(df["Job Description"])
    
    def fit_transform(self,df: pd.DataFrame):
        return self.vectorizer.fit_transform(df["Job Description"])
    
        