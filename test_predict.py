from src.predict import SalaryPredictor

predictor=SalaryPredictor()

job={
    "Rating": 4.2,

    "Size": "1001 to 5000 employees",

    "Type of ownership": "Company - Private",

    "Industry": "Information Technology",

    "Sector": "Information Technology",

    "Revenue": "$100 to $500 million (USD)",

    "Location": "New York, NY",

    "Job Description": """

    Looking for a Data Scientist with

    Python, Machine Learning,

    SQL and AWS experience.

    """
}

salary=predictor.predict(job)
print(f"Predicted Salary: ${salary:,.0f}")
