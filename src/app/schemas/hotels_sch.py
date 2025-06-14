from marshmallow import Schema, fields

class HotelSchema(
    Schema
):
    """
    Schema for registering Hotels
    """
    id = fields.Int()
    name = fields.Str()
    city = fields.Str()
    address = fields.Str()
    stars = fields.Int()
    phone = fields.Str()
    email = fields.Email()
    website = fields.Url()

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)