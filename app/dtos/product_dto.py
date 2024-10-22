from marshmallow import Schema, fields

class ProductDTO(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)
    stock = fields.Number(required=True)
