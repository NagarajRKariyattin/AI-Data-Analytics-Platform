import pandas as pd


def detect_chart_type(df):
    """
    Detect the best chart type based on DataFrame columns.
    """

    if df.empty:
        return None

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    non_numeric_cols = [
        c for c in df.columns
        if c not in numeric_cols
    ]

    # Date column
    for col in non_numeric_cols:
        if "date" in col.lower() or "month" in col.lower():
            if len(numeric_cols) >= 1:
                return "line"

    # One category + one numeric
    if len(non_numeric_cols) == 1 and len(numeric_cols) == 1:

        if len(df) <= 8:
            return "pie"

        return "bar"

    # Two numeric columns
    if len(numeric_cols) == 2:
        return "scatter"

    return None