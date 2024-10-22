from flask import current_app
from bson import ObjectId

# Obtener productos con filtro y paginación
def get_products_by_filter(filter_field, filter_value, page, page_size):
    query = {}
    if filter_field and filter_value:
        query[filter_field] = filter_value
    
    skip = (page - 1) * page_size
    return list(current_app.db.products.find(query).skip(skip).limit(page_size))

# Actualización parcial de producto
def update_partial_product(product_id, updated_data):
    return current_app.db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": updated_data}
    )

def get_product_by_id(product_id):
    return current_app.db.products.find_one({"_id": ObjectId(product_id)})

def add_product(product_data):
    return current_app.db.products.insert_one(product_data).insert_id

def update_product(product_id, updated_data):
    return current_app.db.products.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})

def delet_product(product_id):
    return current_app.db.products.delete_one({"_id": product_id})
