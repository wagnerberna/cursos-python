from db import conn
from mysql.connector import ProgrammingError

# paginação:
# OFFSET indica o início da leitura, e o
# LIMIT o máximo de registros a serem lidos.
sql = "SELECT * FROM hoteis LIMIT 10"
args = 10

with conn() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(list(result))

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        for el in result:
            print(
                f"Hotel: {el[0]} - Nome:{el[1]} -Estrelas:{el[2]} -Diaria:{el[3]} -Cidade:{el[4]}"
            )
