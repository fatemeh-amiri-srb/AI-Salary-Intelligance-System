import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class CategoricalEncoder:
    def __init__(self):
        self.encoder=OneHotEncoder(handle_unknown="ignore",sparse_output=True)
    
    def fit(self,df:pd.DataFrame):
        self.encoder.fit(df)
        return self
    def transform(self,df:pd.DataFrame):
        return self.encoder.transform(df)
    def fit_transform(self,df:pd.DataFrame):
        return self.encoder.fit_transform(df)
    
    
