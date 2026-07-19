import pandas as pd

from src.database.connection import get_connection


def execute_sql(sql_query):
    """
    Executes a SQL query and returns the result as a pandas DataFrame.
    """

    conn = get_connection()

    try:
        df = pd.read_sql_query(sql_query, conn)
        return df

    finally:
        conn.close()