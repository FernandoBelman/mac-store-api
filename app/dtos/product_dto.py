from marshmallow import Schema, fields

class ProductDTO(Schema):
    _id = fields.Str(required=False)  # El ID puede no estar presente al crear un nuevo producto
    name = fields.Str(required=True)
    category = fields.Str(required=False)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
