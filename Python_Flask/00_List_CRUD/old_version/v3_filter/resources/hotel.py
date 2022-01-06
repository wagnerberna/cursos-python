from flask_restful import Resource

from resources.lista_teste import lista_hoteis

# print(lista_hoteis)


class Hoteis(Resource):
    def get(self):
        return {"hoteis": lista_hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        # print(f"get teste ID: {hotel_id}")
        hotel_filter = list(
            filter(lambda hotel: hotel["hotel_id"] == hotel_id, lista_hoteis)
        )
        # print(hotel_filter)
        if hotel_filter:
            return {"hotel": hotel_filter}
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
