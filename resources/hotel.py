from flask_restful import Resource
import json

with open("./data/data.json", 'r') as arquivo:
    json_hoteis = json.load(arquivo)


class Hoteis(Resource):
    #
    def get(self):
        return json_hoteis, 201

class Hotel(Resource):
    #
    def get(self, hotel_id):
        for hotel in json_hoteis["hoteis"]:
            if hotel["hotel_id"] == hotel_id:
                return hotel, 200
        return { "message" : "Hotel not found."}, 404
