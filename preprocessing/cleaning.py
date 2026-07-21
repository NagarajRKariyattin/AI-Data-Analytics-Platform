import pandas as pd


def remove_duplicates(df):
    """
    Removes duplicate rows from the dataset.

    Returns:
        cleaned dataframe
        number of duplicates removed
    """

    before = len(df)

    df = df.drop_duplicates()

    removed = before - len(df)

    return df, removed


def fill_missing_values(
    df,
    numeric_method="median",
    text_method="mode"
):
    """
    Fill missing values using selected methods.

    Numeric:
        mean
        median
        mode
        drop

    Text:
        mode
        unknown
        drop
    """

    df = df.copy()

    filled = 0

    for column in df.columns:

        if df[column].isnull().sum() == 0:
            continue

        # -------------------------
        # Numeric Columns
        # -------------------------
        if pd.api.types.is_numeric_dtype(df[column]):

            if numeric_method == "mean":
                value = df[column].mean()

            elif numeric_method == "median":
                value = df[column].median()

            elif numeric_method == "mode":
                value = df[column].mode().iloc[0]

            elif numeric_method == "drop":

                before = len(df)

                df = df.dropna(subset=[column])

                filled += before - len(df)

                continue

            filled += df[column].isnull().sum()

            df[column] = df[column].fillna(value)

        # -------------------------
        # Text Columns
        # -------------------------
        else:

            if text_method == "mode":

                if not df[column].mode().empty:
                    value = df[column].mode().iloc[0]
                else:
                    value = "Unknown"

            elif text_method == "unknown":

                value = "Unknown"

            elif text_method == "drop":

                before = len(df)

                df = df.dropna(subset=[column])

                filled += before - len(df)

                continue

            filled += df[column].isnull().sum()

            df[column] = df[column].fillna(value)

    return df, filled


def standardize_text(df):
    """
    Standardizes all text columns.

    Example:

        bangalore

        BANGALORE

         Bangalore

    becomes

        Bangalore
    """

    df = df.copy()

    columns_cleaned = 0

    for column in df.select_dtypes(include="object"):

        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
            .str.title()
        )

        columns_cleaned += 1

    return df, columns_cleaned