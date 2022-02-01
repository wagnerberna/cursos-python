from db import new_connection
from mysql.connector import ProgrammingError

drop_tabela_emails = "DROP TABLE IF EXISTS emails"

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(drop_tabela_emails)
    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
