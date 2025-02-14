from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
import json

with open("data/data.json", 'r') as arquivo:
    json_hoteis = json.load(arquivo)

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hotel/<string:hotel_id>")

if __name__ == "__main__":
    app.run(debug = True)