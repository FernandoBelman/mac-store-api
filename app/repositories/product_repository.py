from flask import current_app
from bson import ObjectId

# Obtener productos con filtro y paginación
def get_products_by_filter(query, skip, limit):
    return list(current_app.db.products.find(query).skip(skip).limit(limit))

# Obtener un producto por ID
def get_product_by_id(product_id):
    return current_app.db.products.find_one({"_id": ObjectId(product_id)})

# Crear un nuevo producto
def add_product(product_data):
    return current_app.db.products.insert_one(product_data)

# Actualizar un producto completo
def update_product(product_id, updated_data):
    return current_app.db.products.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})

# Actualización parcial de un producto
def update_partial_product(product_id, updated_data):
    return current_app.db.products.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})

# Eliminar un producto
def delete_product(product_id):
    return current_app.db.products.delete_one({"_id": ObjectId(product_id)})
