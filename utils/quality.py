import pandas as pd

def calculate_quality(df):
    """
    Calculate dataset quality metrics.
    """

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns

    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    if total_cells == 0:
        quality = 0
    else:
        quality = round(
            (1 - ((missing + duplicates) / total_cells)) * 100,
            2
        )

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing": missing,
        "duplicates": duplicates,
        "quality": quality
    }