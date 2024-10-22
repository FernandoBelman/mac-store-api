from app.dtos.product_dto import ProductDTO

# Convierte un producto de MongoDB (formato de entidad) a un DTO
def to_dto(product):
    return {
        '_id': str(product['_id']),
        'name': product['name'],
        'category': product.get('category', None),
        'price': product['price'],
        'stock': product['stock']
    }

# Convierte un DTO a un producto en formato entidad para la base de datos
def to_entity(product_dto):
    return {
        'name': product_dto['name'],
        'category': product_dto.get('category', None),
        'price': product_dto['price'],
        'stock': product_dto['stock']
    }
