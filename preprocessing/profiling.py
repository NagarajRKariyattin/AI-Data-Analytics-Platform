import pandas as pd


def dataset_profile(df):
    """
    Generate a complete profile of the dataset.
    """

    # Basic Information
    total_rows = df.shape[0]
    total_columns = df.shape[1]

    # Missing Values
    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()

    # Duplicate Rows
    duplicate_rows = df.duplicated().sum()

    # Data Types
    data_types = df.dtypes.astype(str)

    # Summary Statistics
    summary = df.describe(include="all")

    # Memory Usage (KB)
    memory_usage = round(df.memory_usage(deep=True).sum() / 1024, 2)

    # Quality Score
    total_cells = total_rows * total_columns

    quality_score = round(
        (
            1 - ((total_missing + duplicate_rows) / total_cells)
        ) * 100,
        2
    )

    profile = {
        "Rows": total_rows,
        "Columns": total_columns,
        "Column Names": list(df.columns),
        "Data Types": data_types,
        "Missing Values": missing_values,
        "Total Missing": total_missing,
        "Duplicate Rows": duplicate_rows,
        "Summary": summary,
        "Memory Usage (KB)": memory_usage,
        "Quality Score": quality_score
    }

    return profile