from db import new_connection
from mysql.connector import ProgrammingError

# like todos q têm ca no nome em qualquer posição
sql = "SELECT * FROM contatos WHERE nome like '%ca%'"
# be no começo
# sql = "SELECT * FROM contatos WHERE nome like 'be%'"

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        for el in cursor:
            print(el)
