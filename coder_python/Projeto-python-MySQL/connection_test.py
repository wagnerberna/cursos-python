from db import new_connection

# with para liberar recursos após uso
with new_connection() as conn:
    if conn.is_connected():
        print("Conectado")

print("Fim")
