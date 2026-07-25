import pandas as pd


def execute_query(conn, sql):

    return pd.read_sql_query(
        sql,
        conn
    )