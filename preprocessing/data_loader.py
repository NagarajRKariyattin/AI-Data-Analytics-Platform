import pandas as pd

def load_data(file):
    """
    Load CSV or Excel files with automatic encoding detection.
    """

    if file.name.endswith(".csv"):

        encodings = ["utf-8", "cp1252", "latin1"]

        for encoding in encodings:
            try:
                file.seek(0)
                return pd.read_csv(file, encoding=encoding)
            except UnicodeDecodeError:
                continue

        raise ValueError("Unsupported CSV encoding.")

    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)

    else:
        raise ValueError("Unsupported file format.")