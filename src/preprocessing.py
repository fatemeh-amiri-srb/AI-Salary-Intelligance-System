from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical variables
    """

    categorical_cols = ["job_title", "company", "location"]

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    return df