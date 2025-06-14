from marshmallow import Schema, fields, validate

class RegisterUserSchema(Schema):
    """
    Schema for registering users
    """
    id = fields.Int()
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    full_name = fields.Str(required=True)
    phone = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    role = fields.Str(required=True, validate=validate.OneOf(["user", "enterprise"]))
register_user_schema = RegisterUserSchema()

class RegisterEnterpriseSchema(Schema): pass


class LoginUserSchema(Schema):
    """
    Schema to login (email & password)
    """
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
login_user_schema = LoginUserSchema()

class LoginEnterpriseSchema(Schema): pass