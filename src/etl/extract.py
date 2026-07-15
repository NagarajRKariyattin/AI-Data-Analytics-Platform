from pathlib import Path
import pandas as pd


def extract_data():
    """
    Reads the first CSV file from data/raw
    and returns a pandas DataFrame.
    """

    base_dir = Path(__file__).resolve().parents[2]

    raw_data = base_dir / "data" / "raw"

    csv_files = list(raw_data.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV file found in data/raw")

    dataset = csv_files[0]

    print(f"Reading file: {dataset.name}")

    df = pd.read_csv(dataset, encoding="latin1")

    return df
    print(df)