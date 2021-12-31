# importar biblioteca de conexão
from mysql.connector import connect

conn = connect(
    host="localhost",
    port=3306,
    user="root",
    password="123",
    database="agenda",
    auth_plugin="mysql_native_password",
)

print(conn)
