import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV

from preprocessing import load_and_clean, scale_features
from feature_engineering import create_features


DATA_PATH = "../data/crypto.csv"


def main():
    print("Loading dataset...")
    df = load_and_clean(DATA_PATH)

    print("Creating features...")
    df = create_features(df)

    print("Dataset shape after feature engineering:", df.shape)

    if len(df) < 50:
        print("Dataset too small after feature engineering!")
        return

    num_cols = ['open','high','low','close','volume','market_cap']
    df, scaler = scale_features(df, num_cols)

    features = [
    'open','high','low','close','volume','market_cap'
    ]

    X = df[features]
    y = df['volatility']

    # Check for bad values
    print("Checking for NaN:", X.isna().sum().sum())
    print("Checking for Inf:", np.isinf(X).sum().sum())

    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    print("Training size:", X_train.shape)
    print("Test size:", X_test.shape)

    param_grid = {
    "n_estimators": [100],
    "max_depth": [10]
}

    grid = GridSearchCV(
        RandomForestRegressor(random_state=42),
        param_grid,
        cv=3,
        scoring="r2",
        n_jobs=-1,
        error_score="raise"   # shows real error if exists
    )

    print("Starting GridSearch...")
    grid.fit(X_train, y_train)

    model = grid.best_estimator_

    pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)

    print("\nBest Params:", grid.best_params_)
    print("RMSE:", rmse)
    print("MAE:", mae)
    print("R2:", r2)

    joblib.dump(model, "../volatility_model.pkl")
    joblib.dump(scaler, "../scaler.pkl")

    print("\nModel saved successfully!")


if __name__ == "__main__":
    main()
