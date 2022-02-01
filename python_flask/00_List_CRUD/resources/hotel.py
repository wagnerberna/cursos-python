from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from resources.lista_teste import lista_hoteis


class Hoteis(Resource):
    def get(self):
        return {"hoteis": lista_hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diarias")
    argumentos.add_argument("cidade")

    def find_hotel(hotel_id):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        instancia_hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = instancia_hotel_objeto.json()

        lista_hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        instancia_hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = instancia_hotel_objeto.json()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        lista_hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global lista_hoteis
        lista_hoteis = [
            el for el in lista_hoteis if el["hotel_id"] != hotel_id
        ]
        return {"message": "hotel deleted"}
