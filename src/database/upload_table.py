from src.database.connection import get_engine


def upload_dataframe(df, table_name):
    """
    Upload a pandas DataFrame to PostgreSQL.
    """

    engine = get_engine()
    df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_", regex=False)
)
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    return True