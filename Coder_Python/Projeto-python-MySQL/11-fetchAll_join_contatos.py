from db import new_connection
from mysql.connector import ProgrammingError

sql = "SELECT * FROM contatos"

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
        print(list(contatos))

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:

        for el in contatos:
            print("\t".join(str(campo) for campo in el))
