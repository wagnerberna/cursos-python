from flask_restful import Resource

from resources.lista_teste import lista_hoteis

# print(lista_hoteis)


class Hoteis(Resource):
    def get(self):
        return {"hoteis": lista_hoteis}
