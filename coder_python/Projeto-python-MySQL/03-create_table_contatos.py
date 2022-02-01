from db import new_connection
from mysql.connector import ProgrammingError

# const com a query a ser executada
tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50), tel VARCHAR(40)
    )
"""

tabela_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""
try:
    with new_connection() as conn:
        try:
            # executa a query
            cursor = conn.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f"Erro: {e.msg}")
except ProgrammingError as e:
    print(f"Erro CONEXÃO: {e.msg}")
