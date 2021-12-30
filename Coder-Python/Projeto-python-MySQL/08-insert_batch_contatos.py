from db import new_connection
from mysql.connector import ProgrammingError


sql = "INSERT INTO contatos (nome, tel) VALUES (%s, %s)"
args = (
    ("Ana", "96765-4321"),
    ("Bia", "97765-4321"),
    ("Luca", "89765-4321"),
    ("Lu", "98765-4321"),
    ("Gui", "98735-4321"),
    ("Beca", "98765-2221"),
    ("Pedro", "98765-6721"),
)

# executeMany
with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        conn.commit()

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print("Registros inclúidos:", cursor.rowcount)
