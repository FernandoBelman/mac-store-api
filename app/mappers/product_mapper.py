from app.dtos.product_dto import ProductDto
from app.models.product_model import Product

def to_dto(product: Product) -> ProductDto:
    return ProductDto(
        id=str(product['_id']),
        name=product['name'],
        description=product['description'],
        price=product['price'],
    )

def to_entity(product_dto: ProductDto) -> Product:
    return {
        'name': product_dto.name,
        'description': product_dto.description,
        'price': product_dto.price,
    }
