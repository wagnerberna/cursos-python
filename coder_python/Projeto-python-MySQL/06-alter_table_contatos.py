from db import new_connection
from mysql.connector import ProgrammingError

alter_tables = (
    "ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
)

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(alter_tables)
        for i, table in enumerate(cursor, start=1):
            print(f"Tabela {i}: {table}")

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
