import sqlite3


def create_connection():

    conn = sqlite3.connect(
        "business.db",
        check_same_thread=False
    )

    return conn