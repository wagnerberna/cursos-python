from db import new_connection
from mysql.connector import ProgrammingError


sql = "INSERT INTO contatos (nome, tel) VALUES (%s, %s)"
args = ("Lucas", "98765-4321")

# commit efetiva as adições
# caso dê certo chama o else
with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
        id = cursor.lastrowid

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print("1 registro incluído, ID:", id)
