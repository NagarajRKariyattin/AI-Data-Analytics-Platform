import pandas as pd


def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.

    Parameters:
        df (DataFrame): Input dataset

    Returns:
        DataFrame: Cleaned dataset
        int: Number of duplicate rows removed
    """

    df = df.copy()

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
    Fill missing values using user-selected methods.

    Numeric methods:
        - mean
        - median
        - mode
        - drop

    Text methods:
        - mode
        - unknown
        - drop

    Returns:
        DataFrame
        int: Total missing values filled
    """

    df = df.copy()

    filled = 0

    for column in df.columns:

        # Skip columns without missing values
        if df[column].isnull().sum() == 0:
            continue

        # ----------------------------
        # Numeric Columns
        # ----------------------------
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

            else:
                value = df[column].median()

            filled += df[column].isnull().sum()

            df[column] = df[column].fillna(value)

        # ----------------------------
        # Text Columns
        # ----------------------------
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

            else:
                value = "Unknown"

            filled += df[column].isnull().sum()

            df[column] = df[column].fillna(value)

    return df, filled


def standardize_text(df):
    """
    Standardize text columns.

    Example:
        " bangalore "
        "BANGALORE"
        "bangalore"

    becomes

        "Bangalore"

    Returns:
        DataFrame
        int: Number of text columns standardized
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


def convert_date_columns(df):
    """
    Automatically detect and convert date columns.

    Returns:
        DataFrame
        int: Number of date columns converted
    """

    df = df.copy()

    converted = 0

    possible_date_columns = [
        "date",
        "order date",
        "invoice date",
        "purchase date",
        "ship date",
        "delivery date"
    ]

    for column in df.columns:

        column_name = column.lower()

        if any(keyword in column_name for keyword in possible_date_columns):

            try:
                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

                converted += 1

            except Exception:
                pass

    return df, converted


def convert_numeric_columns(df):
    """
    Convert numeric-looking text columns into numeric values.

    Example:
        ₹12,500
        15,200
        $450

    becomes

        12500
        15200
        450

    Returns:
        DataFrame
        int: Number of numeric columns converted
    """

    df = df.copy()

    converted = 0

    for column in df.select_dtypes(include="object"):

        try:

            cleaned = (
                df[column]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("₹", "", regex=False)
                .str.replace("$", "", regex=False)
                .str.strip()
            )

            numeric = pd.to_numeric(
                cleaned,
                errors="coerce"
            )

            if numeric.notna().sum() > 0:

                df[column] = numeric

                converted += 1

        except Exception:
            pass

    return df, converted