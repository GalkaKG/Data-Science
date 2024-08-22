import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load data from a CSV file.

    :param file_path: str, path to the CSV file
    :return: pd.DataFrame, the loaded DataFrame
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Perform data cleaning steps.

    :param df: pd.DataFrame, raw data
    :return: pd.DataFrame, cleaned data
    """
    # Implement your cleaning steps here
    # Example: drop missing values
    df = df.dropna()
    
    # Example: remove unnecessary columns
    # df = df.drop(columns=["unnecessary_column"])
    
    return df

def scale_data(df):
    """
    Scale the numeric features in the data using StandardScaler.

    :param df: pd.DataFrame, data to scale
    :return: pd.DataFrame, scaled data
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    
    # Convert back to DataFrame with original columns
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    return scaled_df
