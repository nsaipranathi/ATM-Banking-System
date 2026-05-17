# =========================================
# STREAMLIT APP - app.py
# =========================================
# Required: pip install streamlit pandas numpy scikit-learn

import streamlit as st
import pandas as pd
import numpy as np

try:
    from sklearn.model_selection import train_test_split  # type: ignore[reportMissingModuleSource]
    from sklearn.preprocessing import LabelEncoder  # type: ignore[reportMissingModuleSource]
    from sklearn.ensemble import RandomForestClassifier  # type: ignore[reportMissingModuleSource]
except Exception:
    # If scikit-learn is not available, inform the user and stop the app.
    st.error("scikit-learn is not installed. Please install scikit-learn to run this app.")
    st.stop()

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("Tax.csv")

# Remove unwanted column
df.drop("Unnamed: 0", axis=1, inplace=True)

# =========================================
# ENCODE TARGET COLUMN
# =========================================

le = LabelEncoder()

df["PoliticalParty"] = le.fit_transform(df["PoliticalParty"])

# =========================================
# FEATURES AND TARGET
# =========================================

X = df.drop("PoliticalParty", axis=1)

y = df["PoliticalParty"]

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================================
# TRAIN MODEL
# =========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =========================================
# STREAMLIT UI
# =========================================

st.title("Political Party Prediction App")

st.write("Enter the details below")

# =========================================
# INPUT FIELDS
# =========================================

HHI = st.number_input("Household Income", min_value=0)

HHDL = st.number_input("Household Debt Level", min_value=0)

Married = st.number_input("Married (0 = No, 1 = Yes)", min_value=0, max_value=1)

CollegGrads = st.number_input("Number of College Graduates", min_value=0)

AHHAge = st.number_input("Average Household Age", min_value=0)

Cars = st.number_input("Number of Cars", min_value=0)

Filed2017 = st.number_input("Filed in 2017 (0 or 1)", min_value=0, max_value=1)

Filed2016 = st.number_input("Filed in 2016 (0 or 1)", min_value=0, max_value=1)

Filed2015 = st.number_input("Filed in 2015 (0 or 1)", min_value=0, max_value=1)

# =========================================
# PREDICTION BUTTON
# =========================================

if st.button("Predict"):

    input_data = np.array([[HHI,
                            HHDL,
                            Married,
                            CollegGrads,
                            AHHAge,
                            Cars,
                            Filed2017,
                            Filed2016,
                            Filed2015]])

    prediction = model.predict(input_data)

    labels = {
        0: "Democrat",
        1: "Independent",
        2: "Republican"
    }

    result = labels[prediction[0]]

    st.success(f"Predicted Political Party: {result}")