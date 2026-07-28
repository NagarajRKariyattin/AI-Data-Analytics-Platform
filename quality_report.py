import pandas as pd


def generate_quality_report(df):

    report = {}

    report["Rows"] = len(df)
    report["Columns"] = len(df.columns)

    report["Missing Values"] = int(df.isnull().sum().sum())

    report["Duplicate Rows"] = int(df.duplicated().sum())

    report["Numeric Columns"] = len(
        df.select_dtypes(include="number").columns
    )

    report["Text Columns"] = len(
        df.select_dtypes(include="object").columns
    )

    report["Date Columns"] = len(
        [
            col for col in df.columns
            if "date" in col.lower()
            or "month" in col.lower()
            or "year" in col.lower()
        ]
    )

    report["Outlier Columns"] = []

    numeric_df = df.select_dtypes(include="number")

    for col in numeric_df.columns:

        q1 = numeric_df[col].quantile(0.25)
        q3 = numeric_df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        if ((numeric_df[col] < lower) | (numeric_df[col] > upper)).any():

            report["Outlier Columns"].append(col)

    return report