from sqlalchemy import inspect
from src.database.connection import get_engine


def get_schema(table_name):
    """
    Returns schema information for a PostgreSQL table.
    """

    engine = get_engine()

    inspector = inspect(engine)

    columns = inspector.get_columns(table_name)

    schema = []

    for column in columns:
        schema.append({
            "name": column["name"],
            "type": str(column["type"])
        })

    return schema