from marshmallow import Schema, fields, validate

class UserSchema(
    Schema
):
    id = fields.Int()
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    full_name = fields.Str(required=True)
    phone = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    role = fields.Str(required=True, validate=validate.OneOf(["user", "enterprise"]))

user_schema = UserSchema()