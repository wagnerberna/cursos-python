from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from old_version.lista_teste import lista_hoteis
from db import conn


class Hoteis(Resource):
    def get(self):
        sql = "SELECT * FROM hoteis"
        # args = 50
        global conn
        with conn() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            hoteis = cursor.fetchall()
            # print(hoteis)
            return {"hoteis": hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

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
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {"message": "hotel deleted"}
        return {"message": "Hotel not found"}, 404
