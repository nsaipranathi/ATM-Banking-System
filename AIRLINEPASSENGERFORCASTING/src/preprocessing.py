# Scaling & preprocessing
 
"""
====================================================
Module : preprocessing.py
Project: Airline Passenger Forecasting
Purpose: Scale the dataset using MinMaxScaler
====================================================
"""
 
# Import required libraries
import pickle
try:
    import pandas as pd
except ImportError:
    raise ImportError("pandas is required to run this module. Install it with: pip install pandas")
 
from sklearn.preprocessing import MinMaxScaler
 
 
class Preprocessor:
    """
    Preprocess the time series dataset.
    """
 
    def __init__(self):
        """
        Initialize the scaler.
        """
 
        self.scaler = MinMaxScaler(feature_range=(0, 1))
 
    def scale_data(self, df):
        """
        Scale the Passengers column.
 
        Parameters
        ----------
        df : pandas.DataFrame
 
        Returns
        -------
        scaled_df : pandas.DataFrame
        """
 
        print("\nOriginal Data")
        print(df.head())
 
        # Scale the Passengers column
        scaled_values = self.scaler.fit_transform(df[["Passengers"]])
 
        # Convert to DataFrame
        scaled_df = pd.DataFrame(
            scaled_values,
            columns=["Passengers"],
            index=df.index
        )
 
        # print("\nScaled Data")
        # print(scaled_df.head())
 
        # Save the scaler
        with open("models/scaler.pkl", "wb") as f:
            pickle.dump(self.scaler, f)
 
        print("\nScaler saved successfully.")
 
        return scaled_df
 
if __name__ == "__main__":
 
    from data_loader import DataLoader
 
    DATA_PATH = (r"data/airline_passengers.csv")
 
    # Load data
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()
 
    # Scale data
    preprocessor = Preprocessor()
 
    scaled_df = preprocessor.scale_data(df)
 
    print("\nScaled Dataset")
    print(scaled_df.head())