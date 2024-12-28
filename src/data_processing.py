import pandas as pd

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocesses the data by adding derived columns."""
    df['SHOT_ATTEMPTED'] = 1
    df['SHOT_MADE'] = df['SCORE'].apply(lambda x: 1 if x == 'MADE' else 0)
    df['DISTANCE'] = (df['X']**2 + df['Y']**2)**0.5
    return df