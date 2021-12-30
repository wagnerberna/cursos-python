from db import new_connection
from mysql.connector import ProgrammingError

sql = "SELECT * FROM contatos WHERE nome like %s"

with new_connection() as conn:
    try:
        nome = input("contato p/ localizar: ")
        # args entre % % q define o tipo de busca do like
        args = (f"%{nome}%",)
        cursor = conn.cursor()
        cursor.execute(sql, args)

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        for el in cursor:
            print(el)
