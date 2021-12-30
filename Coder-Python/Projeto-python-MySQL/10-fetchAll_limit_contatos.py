from db import new_connection
from mysql.connector import ProgrammingError

# paginação:
# OFFSET indica o início da leitura, e o
# LIMIT o máximo de registros a serem lidos.
sql = "SELECT * FROM contatos LIMIT %s OFFSET %s"
args = (10, 5)

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall()
        print(list(contatos))

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        # 2d 10s número de caracteres a ser exibido
        for el in contatos:
            print(f"ID:{el[0]:2d} - Nome:{el[1]:10s} -Telefone:{el[2]}")
