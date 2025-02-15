from flask_restful import Resource, reqparse
from models.hotelmodel import HotelModel
import json

with open("./db_files/db_files.json", 'r') as arquivo:
    json_hoteis = json.load(arquivo)

class Hoteis(Resource):
    def get(self):
        return json_hoteis, 201

class Hotel(Resource):
    def encontrar_hotel(self, hotel_id):
        for hotel in json_hoteis["hoteis"]:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.encontrar_hotel(hotel_id)
        if hotel:
            return hotel
        return { "message" : "Hotel not found."}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("nome")
        argumentos.add_argument("estrelas")
        argumentos.add_argument("diaria")
        argumentos.add_argument("cidade")
        dados = argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        json_hoteis["hoteis"].append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("nome", type=str, required=True)
        argumentos.add_argument("estrelas", type=int, required=True)
        argumentos.add_argument("diaria", type=float, required=True)
        argumentos.add_argument("cidade", type=str, required=True)
        dados = argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = self.encontrar_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        else:
            json_hoteis["hoteis"].append(novo_hotel)
            return novo_hotel, 201 # Criando novo hotel com sucesso

    def delete(self, hotel_id):
        global json_hoteis
        json_hoteis["hoteis"] = [hotel for hotel in json_hoteis["hoteis"] if hotel["hotel_id"] != hotel_id]
        return {"message": "Hotel deleted"}
