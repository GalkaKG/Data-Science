import pandas as pd

def create_features(df):
    """
    Create new features or transform existing ones.

    :param df: pd.DataFrame, input data
    :return: pd.DataFrame, data with new features
    """
    # Example: Create interaction terms
    df['BMI_Age'] = df['BMI'] * df['Age']
    
    # Example: Create binary indicators
    df['High_BMI'] = (df['BMI'] > 30).astype(int)
    
    return df

def select_features(df, features):
    """
    Select a subset of features for the final model.

    :param df: pd.DataFrame, input data
    :param features: list of str, list of feature names to keep
    :return: pd.DataFrame, data with selected features
    """
    return df[features]
