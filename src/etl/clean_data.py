import pandas as pd


def clean_data(df):
    """Clean a dataset by removing duplicates and empty rows."""
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df