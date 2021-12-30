from db import new_connection
from mysql.connector import ProgrammingError

sql = "UPDATE contatos SET nome= %s WHERE id = %s"
# args = ('Aline', )

# commit efetiva a exclusão
with new_connection() as conn:
    try:
        id = input("Digite o id do contato para atualizar: ")
        nome_update = input("Digite o novo nome: ")
        args = (nome_update, id)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()

    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print(f"{cursor.rowcount} registro(s) alterado(s).")
