import pandas as pd


def load_csv(uploaded_file):
    """
    Read uploaded CSV file.
    """

    df = pd.read_csv(uploaded_file)

    return df