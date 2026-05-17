import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    from sklearn.ensemble import RandomForestRegressor  # pyright: ignore[reportMissingModuleSource]
    from sklearn.preprocessing import LabelEncoder  # pyright: ignore[reportMissingModuleSource]
    try:
        from sklearn.metrics import (  # pyright: ignore[reportMissingModuleSource]
            mean_absolute_error,
            mean_squared_error,
            r2_score
        )
    except Exception:
        # Provide lightweight metric implementations if sklearn.metrics is not available
        def mean_absolute_error(y_true, y_pred):
            return float(np.mean(np.abs(np.array(y_true) - np.array(y_pred))))

        def mean_squared_error(y_true, y_pred):
            return float(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))

        def r2_score(y_true, y_pred):
            y_true = np.array(y_true)
            y_pred = np.array(y_pred)
            ss_res = np.sum((y_true - y_pred) ** 2)
            ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
            return float(1 - ss_res / ss_tot) if ss_tot != 0 else 0.0
except Exception:
    st.error("scikit-learn is not available. Please install scikit-learn to use this app (pip install scikit-learn).")
    raise SystemExit


def train_test_split(X, y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    test_count = max(1, int(len(X) * test_size))
    test_indices = indices[:test_count]
    train_indices = indices[test_count:]

    return (
        X.iloc[train_indices],
        X.iloc[test_indices],
        y.iloc[train_indices],
        y.iloc[test_indices],
    )

# Title
st.title("Random Forest Regression")

# Upload File
uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file is not None:

    # Read Dataset
    data = pd.read_excel(uploaded_file)

    st.subheader("Dataset")
    st.write(data.head())

    # Remove Missing Values
    data = data.dropna()

    # Remove Duplicates
    data = data.drop_duplicates()

    st.subheader("Dataset Shape")
    st.write(data.shape)

    st.subheader("Column Names")
    st.write(data.columns)

    # Encode Categorical Column
    le = LabelEncoder()
    data['Class'] = le.fit_transform(data['Class'])

    # Features and Target
    X = data.drop('Class', axis=1)
    y = data['Class']

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Build Model
    rf = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # Train Model
    rf.fit(X_train, y_train)

    # Predictions
    y_pred = rf.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    st.subheader("Model Evaluation")

    st.write(f"Mean Absolute Error : {mae}")
    st.write(f"Mean Squared Error : {mse}")
    st.write(f"Root Mean Squared Error : {rmse}")
    st.write(f"R2 Score : {r2}")

    # Feature Importance
    importance = rf.feature_importances_

    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': importance
    })

    feature_importance = feature_importance.sort_values(
        by='Importance',
        ascending=False
    )

    st.subheader("Feature Importance")
    st.write(feature_importance)



    ax1.set_title("Feature Importance - Random Forest")

    st.pyplot(fig1)

    # Actual vs Predicted Plot
    fig2, ax2 = plt.subplots(figsize=(8, 6))

    ax2.scatter(y_test, y_pred)

    ax2.set_xlabel("Actual Values")
    ax2.set_ylabel("Predicted Values")
    ax2.set_title("Actual vs Predicted")

    st.pyplot(fig2)