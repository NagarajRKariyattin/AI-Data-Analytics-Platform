import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="ai_data_analytics",
        user="postgres",
        password="Nagu@6363"
    )
    return conn