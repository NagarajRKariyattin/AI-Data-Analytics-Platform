from sqlalchemy import create_engine
import pandas as pd
from src.database.connection import get_engine
 
def load_dataframe(df, table_name):
    """
    Load any DataFrame into PostgreSQL.
    """

    engine = get_engine()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"\nTable '{table_name}' created successfully.")
    print(f"{len(df)} records inserted.")