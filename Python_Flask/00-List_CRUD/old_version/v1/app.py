from flask import Flask
from flask_restful import Resource, Api

# api faz todo gerenciamento de como funciona
app = Flask(__name__)
api = Api(app)

# estende "herda" a classe Resource
class Hoteis(Resource):
    def get(self):
        return {"hotel": "nome"}


# adicionar o recurso(nome_classe e endpoint)
api.add_resource(Hoteis, "/hoteis")

# config básica do flask
# se app.py for principal
# debug True até terminar o ambiente de produção, depois False.
if __name__ == "__main__":
    app.run(debug=True)
