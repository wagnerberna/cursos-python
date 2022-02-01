from db import new_connection
from mysql.connector import ProgrammingError

sql = "SELECT * FROM contatos"

# fetchone - busca 1 resultado em seq. se usar + vezes
with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        # contatos = cursor.fetchone()

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print(cursor.fetchone())
        print(cursor.fetchone())
        print(cursor.fetchone())
