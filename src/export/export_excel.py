import io
import pandas as pd


def export_to_excel(df):
    """
    Convert DataFrame to Excel bytes.
    """

    # Make a copy so the original DataFrame isn't modified
    df = df.copy()

    # Remove timezone information from datetime columns
    for col in df.columns:
        if pd.api.types.is_datetime64tz_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Query Result")

    buffer.seek(0)

    return buffer.getvalue()