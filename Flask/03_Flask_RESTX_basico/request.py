from requests import put, get

# instalar biblioteca requests
# add / get tarefas

put("http://localhost:5000/task5", data={"data": "Derrotar Thanos"}).json()
get("http://localhost:5000/task5").json()

put("http://localhost:5000/task6", data={"data": "Salvar o Mundo"}).json()
get("http://localhost:5000/task6").json()
