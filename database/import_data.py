import pandas as pd


def load_dataframe_to_db(df, conn):

    df.to_sql(
        "orders",
        conn,
        if_exists="replace",
        index=False
    )