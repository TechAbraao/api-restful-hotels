from flask_restful import Resource, reqparse
import json

with open("./data/data.json", 'r') as arquivo:
    json_hoteis = json.load(arquivo)


class Hoteis(Resource):

    def get(self):
        return json_hoteis, 201

class Hotel(Resource):

    def get(self, hotel_id):
        for hotel in json_hoteis["hoteis"]:
            if hotel["hotel_id"] == hotel_id:
                return hotel, 200
        return { "message" : "Hotel not found."}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("nome")
        argumentos.add_argument("estrelas")
        argumentos.add_argument("diaria")
        argumentos.add_argument("cidade")
        dados = argumentos.parse_args()
        novo_hotel = {
            "hotel_id" : hotel_id,
            "nome" : dados["nome"],
            "estrelas" : dados["estrelas"],
            "diaria" : dados["diaria"],
            "cidade" : dados["cidade"]
        }
        json_hoteis["hoteis"].append(novo_hotel)
        return novo_hotel, 200