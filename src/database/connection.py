import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="ai_data_analytics",
        user="postgres",
        password="Nagu@6363"
    )
    return conn

def get_engine():

    url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="Nagu@6363",
        host="localhost",
        port=5432,
        database="ai_data_analytics"
    )

    return create_engine(url)