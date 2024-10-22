from app.repositories.product_repository import *
from app.mappers.product_mapper import to_dto, to_entity
from app.cache import cache_get, cache_set
import json

# Obtener productos con filtro y paginación
def get_paginated_products(page, page_size, field=None, value=None):
    query = {}
    if field and value:
        query[field] = {'$regex': value, '$options': 'i'}  # Filtro insensible a mayúsculas

    skip = (page - 1) * page_size
    products = get_products_by_filter(query, skip, page_size)
    
    # Convertir los productos a DTO
    products_dto = [to_dto(product) for product in products]
    return products_dto

# Obtener producto por ID
def get_product_by_id_service(product_id):
    cached = cache_get(product_id)
    if cached:
        return json.loads(cached)

    product = get_product_by_id(product_id)
    if product:
        product_dto = to_dto(product)
        cache_set(product_id, json.dumps(product_dto))
        return product_dto
    return None

# Crear un nuevo producto
def create_product(data):
    product = to_entity(data)
    result = add_product(product)
    product['_id'] = str(result.inserted_id)
    return product

# Actualizar un producto completo
def update_product_service(product_id, data):
    required_fields = ["name", "price", "category", "stock"]
    missing_fields = [field for field in required_fields if field not in data or data[field] is None]
    
    if missing_fields:
        return None, f"Missing required fields: {', '.join(missing_fields)}"
    
    updated_data = {
        "name": data["name"],
        "price": data["price"],
        "category": data["category"],
        "stock": data["stock"]
    }
    result = update_product(product_id, updated_data)
    return result.matched_count > 0, None

# Actualizar un producto parcialmente
def update_partial_product_service(product_id, data):
    update_data = {key: value for key, value in data.items() if value is not None}
    if not update_data:
        return False, 'No valid fields to update'

    result = update_partial_product(product_id, update_data)
    return result.matched_count > 0, None

# Eliminar un producto
def delete_product_service(product_id):
    result = delete_product(product_id)
    return result.deleted_count > 0
