import pandas as pd

def basic_info(df):
    print("="*50)
    print("Dataset Shape")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())
