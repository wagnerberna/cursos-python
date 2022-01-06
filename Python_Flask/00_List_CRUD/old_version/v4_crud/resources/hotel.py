from flask_restful import Resource, reqparse

from resources.lista_teste import lista_hoteis

# reqparse permite receber JSON da requisição
# print(lista_hoteis)


class Hoteis(Resource):
    def get(self):
        return {"hoteis": lista_hoteis}


class Hotel(Resource):
    # atributos da classe define o Construtor
    # adicionar nos argumentos pelo nome cada um
    # para receber apenas os dados definidos
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    def find_hotel(hotel_id):
        for hotel in lista_hoteis:
            # print(hotel)
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        # chama classe Hotel.fn
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):
        # referencia a classe Hotel
        # kwargs desempacota os dados
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {"hotel_id": hotel_id, **dados}

        lista_hoteis.append(novo_hotel)
        return novo_hotel, 200

    # se hotel existir atualiza, senão cria novo
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {"hotel_id": hotel_id, **dados}

        # update atualiza os dados do hotel localizado
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        # senão encontrar cria
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        # list comp. retorna lista com todos hotéis menos o deletado
        # global ref. a variável como global
        global lista_hoteis
        lista_hoteis = [
            el for el in lista_hoteis if el["hotel_id"] != hotel_id
        ]
        return {"message": "hotel deleted"}
