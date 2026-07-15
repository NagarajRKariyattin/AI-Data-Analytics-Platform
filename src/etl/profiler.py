from src.etl.extract import extract_data


def profile_data(df):

    print("=" * 50)
    print("DATA PROFILE REPORT")
    print("=" * 50)

    print(f"Rows                : {df.shape[0]}")
    print(f"Columns             : {df.shape[1]}")
    print(f"Missing Values      : {df.isnull().sum().sum()}")
    print(f"Duplicate Rows      : {df.duplicated().sum()}")

    memory = df.memory_usage(deep=True).sum() / 1024**2

    print(f"Memory Usage (MB)   : {memory:.2f}")

    numeric = df.select_dtypes(include="number").columns

    categorical = df.select_dtypes(include="object").columns

    print(f"Numeric Columns     : {len(numeric)}")
    print(f"Categorical Columns : {len(categorical)}")


if __name__ == "__main__":

    dataframe = extract_data()

    profile_data(dataframe)