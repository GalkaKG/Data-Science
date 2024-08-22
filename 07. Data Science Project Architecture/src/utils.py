def save_data(df, file_path):
    """
    Save the DataFrame to a CSV file.

    :param df: pd.DataFrame, data to save
    :param file_path: str, path where to save the file
    """
    df.to_csv(file_path, index=False)

def print_dataframe_info(df):
    """
    Print information about the DataFrame.

    :param df: pd.DataFrame
    """
    print(df.head())
    print(df.info())
