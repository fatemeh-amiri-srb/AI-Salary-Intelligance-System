import pandas as pd

def preprocess_tabular(df: pd.DataFrame):
    df_model=df[[
        "Rating",

        "Size",

        "Type of ownership",

        "Industry",

        "Sector",

        "Revenue",

        "Location"        
    ]].copy()

    return df_model