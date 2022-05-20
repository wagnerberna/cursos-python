from db import conn
from mysql.connector.errors import ProgrammingError

database_hotel = "CREATE DATABASE IF NOT EXISTS hotel"
tabela_hoteis = """CREATE TABLE IF NOT EXISTS hoteis(
    id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50) NOT NULL,
    estrelas INT, diaria INT, cidade VARCHAR(50) NOT NULL)"""
insert_hoteis = """INSERT INTO hoteis
    (nome, estrelas, diaria, cidade)
    VALUES (%s, %s, %s, %s)"""
insert_hoteis_args = (
    ("Rio Hotel", 4.3, 345.30, "Rio de Janeiro"),
    ("Gramado Hotel", 5.0, 500.00, "Gramado"),
    ("Rosa Hotel", 3.0, 200.00, "Garopaba"),
)


with conn() as conn:
    try:
        cursor = conn.cursor()
        # cursor.execute(database_hotel)
        # cursor.execute(tabela_hoteis)
        cursor.executemany(insert_hoteis, insert_hoteis_args)
        conn.commit()
    except ProgrammingError as e:
        print(f"Erro: {e.msg}")
    else:
        print("registros incluídos")
