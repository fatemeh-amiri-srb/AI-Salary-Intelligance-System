from src.data_loader import load_data
from src.eda import basic_info

df=load_data("data/raw/glassdoor_jobs.csv")
basic_info(df)