from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

param = dict(
    host="localhost",
    port=3306,
    user="root",
    password="123",
    database="hotel",
    auth_plugin="mysql_native_password",
)


@contextmanager
def conn():
    conn = connect(**param)
    try:
        yield conn
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("finally...")
