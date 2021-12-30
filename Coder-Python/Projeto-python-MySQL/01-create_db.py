from db import new_connection

# print(conn)

with new_connection() as conn:
    # cria o método cursor q executa comandos no banco
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS agenda")
