from flask_restful import Resource

from resources.lista_teste import lista_hoteis

# print(lista_hoteis)


class Hoteis(Resource):
    def get(self):
        return {"hoteis": lista_hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        # print(f"get teste ID: {hotel_id}")
        for hotel in lista_hoteis:
            # print(hotel)
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
