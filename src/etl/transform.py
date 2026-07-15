from pathlib import Path

from src.etl.extract import extract_data


def transform_data(df):
    """
    Cleans the dataset and saves it.
    """

    print("\nCleaning Dataset...")
    print("-" * 50)

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"Removed Duplicate Rows : {duplicates}")

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Save cleaned data
    base_dir = Path(__file__).resolve().parents[2]
    processed_folder = base_dir / "data" / "processed"

    processed_folder.mkdir(exist_ok=True)

    output_file = processed_folder / "cleaned_superstore.csv"

    df.to_csv(output_file, index=False)

    print("\nCleaned dataset saved successfully!")
    print(output_file)

    return df


if __name__ == "__main__":

    dataframe = extract_data()

    transform_data(dataframe)