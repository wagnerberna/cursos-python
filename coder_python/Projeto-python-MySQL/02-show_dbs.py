from db import new_connection

with new_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")

# enumerate() retorna uma tupla de dois elementos a cada iteração:
# um número sequencial e um item da sequência correspondente.
# start inicia o i com 1
for i, database in enumerate(cursor, start=1):
    print(f"Banco de Dados {i}: {database[0]}")
