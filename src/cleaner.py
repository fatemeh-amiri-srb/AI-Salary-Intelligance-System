import pandas as pd
import numpy as np
import re


def clean_salary(df: pd.DataFrame) -> pd.DataFrame:

    df = df[df["Salary Estimate"] != "-1"].copy()

    # flag hourly salaries
    df["hourly"] = df["Salary Estimate"].str.contains("Per Hour", na=False)

    # remove text noise
    salary = (
        df["Salary Estimate"]
        .str.replace(r"\(.*?\)", "", regex=True)
        .str.replace("Employer Provided Salary:", "", regex=False)
        .str.replace("Per Hour", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("K", "", regex=False)
        .str.strip()
    )

    # split range
    salary_split = salary.str.split("-", expand=True)

    df["min_salary"] = salary_split[0].astype(float)
    df["max_salary"] = salary_split[1].astype(float)

    # average salary
    df["avg_salary"] = (df["min_salary"] + df["max_salary"]) / 2

    # convert hourly → yearly
    df["avg_salary"] = np.where(
        df["hourly"] == True,
        df["avg_salary"] * 40 * 52,
        df["avg_salary"] * 1000  # چون K داریم
    )

    return df