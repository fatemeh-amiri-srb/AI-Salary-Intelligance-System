from src.data_loader import load_data
from src.cleaner import clean_salary
from src.build_features import build_features
from src.train import train_model
from src.evaluate import evaluate


# 1. load
df = load_data("data/raw/glassdoor_jobs.csv")

# 2. clean
df = clean_salary(df)

# 3. features
X, encoders, tfidf = build_features(df)

# 4. target
y = df["avg_salary"]

# 5. train
model, X_test, y_test = train_model(X, y)

# 6. evaluate
evaluate(model, X_test, y_test)