# classe de hotel modelo
class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diarias, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diarias = diarias
        self.cidade = cidade

    # converter para dict
    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diarias": self.diarias,
            "cidade": self.cidade,
        }