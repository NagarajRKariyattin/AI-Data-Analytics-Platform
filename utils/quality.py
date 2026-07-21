def calculate_quality(df):
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    quality = round(
        (1 - ((missing + duplicates) / total_cells)) * 100,
        2
    )

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing": int(missing),
        "duplicates": int(duplicates),
        "quality": quality
    }