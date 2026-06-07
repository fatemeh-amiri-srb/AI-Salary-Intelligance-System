import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw Glassdoor data
    """

    df = df.dropna()

    # remove extreme salaries
    df = df[df["salary"] < df["salary"].quantile(0.99)]

    # normalize text
    df["job_title"] = df["job_title"].str.lower()
    df["company"] = df["company"].str.lower()
    df["location"] = df["location"].str.lower()

    return df