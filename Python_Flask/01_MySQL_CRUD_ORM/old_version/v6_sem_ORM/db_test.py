from db import conn

with conn() as conn:
    if conn.is_connected():
        print("conectado")
    print("fim")
