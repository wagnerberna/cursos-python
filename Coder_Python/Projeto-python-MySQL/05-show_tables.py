from db import new_connection
from mysql.connector import ProgrammingError

show_tables = "SHOW TABLES"

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(show_tables)
        for i, table in enumerate(cursor, start=1):
            print(f"Tabela {i}: {table}")

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
