import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load raw Glassdoor dataset
    """
    df = pd.read_csv(path)
    return df