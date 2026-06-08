from src.data_loader import load_data
from src.eda import basic_info
from src.cleaner import clean_salary

df=load_data("data/raw/glassdoor_jobs.csv")
basic_info(df)
# print(df["Salary Estimate"].head(20))
# print(df["Salary Estimate"].sample(20).tolist())

df=clean_salary(df)
df[["Salary Estimate", "hourly", "avg_salary"]].head(10)
print(df["hourly"].value_counts())
print(df["avg_salary"].describe())
# print(df[["Salary Estimate",
#           "min_salary",
#           "max_salary",
#           "salary"]].head(20))
