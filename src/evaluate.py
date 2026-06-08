from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def evaluate(model, X_test, y_test):
    """
    Evaluate regression model performance
    """

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("=" * 40)
    print("MODEL EVALUATION")
    print("=" * 40)

    print(f"MAE  : {mae:,.2f}")
    print(f"RMSE : {rmse:,.2f}")
    print(f"R2   : {r2:.4f}")

    print("=" * 40)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }