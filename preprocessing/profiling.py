import pandas as pd

def dataset_profile(df):

    total_rows = df.shape[0]
    total_columns = df.shape[1]

    missing_values = df.isnull().sum()

    total_missing = missing_values.sum()

    duplicate_rows = df.duplicated().sum()

    quality_score = round(
        (
            1
            - (
                (total_missing + duplicate_rows)
                /
                (total_rows * total_columns)
            )
        ) * 100,
        2
    )

    profile = {
        "Rows": total_rows,
        "Columns": total_columns,
        "Missing Values": missing_values,
        "Total Missing": total_missing,
        "Duplicate Rows": duplicate_rows,
        "Column Names": list(df.columns),
        "Data Types": df.dtypes.astype(str),
        "Summary": df.describe(include="all"),
        "Quality Score": quality_score
    }

    return profile