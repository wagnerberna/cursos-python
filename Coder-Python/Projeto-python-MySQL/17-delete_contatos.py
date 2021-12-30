from db import new_connection
from mysql.connector import ProgrammingError

sql = "DELETE FROM contatos WHERE id = %s"

# commit efetiva a exclusão
with new_connection() as conn:
    try:
        id = input("contato para excluir: ")
        args = (f"{id}",)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print(f"{cursor.rowcount} registro(s) deletado(s).")
