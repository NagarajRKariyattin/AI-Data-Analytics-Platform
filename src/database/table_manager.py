from sqlalchemy import inspect
from src.database.connection import get_engine


def get_table_names():
    """
    Return all tables in the PostgreSQL database.
    """
    engine = get_engine()
    inspector = inspect(engine)

    return inspector.get_table_names()