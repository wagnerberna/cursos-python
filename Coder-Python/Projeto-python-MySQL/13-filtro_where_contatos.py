from db import new_connection
from mysql.connector import ProgrammingError

sql = "SELECT * FROM contatos WHERE tel = '98765-2221'"

with new_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        # print(cursor)

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        for el in cursor:
            print(el)
