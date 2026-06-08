from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib


def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "models/model.pkl")

    return model, X_test, y_test