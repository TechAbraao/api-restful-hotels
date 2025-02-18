from flask_restful import Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.hotelmodel import HotelModel

db = create_engine("sqlite:////home/asantos/courses-udemy-projects/rest-api-flask/db_files/banco.db")
Session = sessionmaker(bind=db)
session = Session()

class Hoteis(Resource):
    def get(self):
        dados = session.query(HotelModel).all()
        dados_json = [hotel.json() for hotel in dados]
        return dados_json, 201

class Hotel(Resource):
    def encontrar_hotel(self, hotel_id):
        hotel = session.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
        if hotel:
            return hotel.json()
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
        novo_hotel = HotelModel(hotel_id=hotel_id, **dados)
        session.add(novo_hotel)
        session.commit()
        return novo_hotel.json(), 200

    def put(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument("nome", type=str, required=True)
        argumentos.add_argument("estrelas", type=int, required=True)
        argumentos.add_argument("diaria", type=float, required=True)
        argumentos.add_argument("cidade", type=str, required=True)
        dados = argumentos.parse_args()
        hotel = session.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()

        if hotel:
            hotel.nome = dados['nome']
            hotel.estrelas = dados['estrelas']
            hotel.diaria = dados['diaria']
            hotel.cidade = dados['cidade']
            session.commit()
            return hotel.json(), 200
        else:
            novo_hotel = HotelModel(hotel_id=hotel_id, **dados)
            session.add(novo_hotel)
            session.commit()
            return novo_hotel.json(), 201

    def delete(self, hotel_id):
        hotel = session.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()
        if hotel:
            session.delete(hotel)
            session.commit()
            return {"message": "Hotel deleted"}, 200
        return {"message": "Hotel not found"}, 404

