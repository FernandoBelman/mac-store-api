from flask import Blueprint, jsonify, request, abort, current_app
from bson import ObjectId

product_bp = Blueprint('product_bp', __name__)

# GET (múltiples elementos con paginación y filtro)
@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        # Obtener parámetros de paginación y filtrado
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        field = request.args.get('field', None)
        value = request.args.get('value', None)

        # Crear la consulta
        query = {}
        if field and value:
            query[field] = {'$regex': value, '$options': 'i'}  # Búsqueda insensible a mayúsculas/minúsculas

        # Ejecutar consulta con paginación
        products_cursor = current_app.db.products.find(query).skip((page - 1) * page_size).limit(page_size)
        products = list(products_cursor)
        
        # Convertir ObjectId a string
        for product in products:
            product['_id'] = str(product['_id'])

        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET: Obtener un producto por ID
@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = current_app.db.products.find_one({"_id": ObjectId(product_id)})
        if not product:
            return jsonify({"error": "Product not found"}), 404
        product['_id'] = str(product['_id'])  # Convertir ObjectId a string
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PATCH: Actualizar propiedades específicas de un producto
@product_bp.route('/products/<product_id>', methods=['PATCH'])
def patch_product(product_id):
    try:
        # Obtener los datos enviados por el usuario
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Filtrar los campos que no son None para actualizar sólo lo que se envió
        update_data = {key: value for key, value in data.items() if value is not None}
        
        if not update_data:
            return jsonify({'error': 'No valid fields to update'}), 400
        
        # Realizar la actualización parcial en la base de datos
        result = current_app.db.products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': update_data}
        )

        if result.matched_count == 0:
            return jsonify({'error': 'Product not found'}), 404
        
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Crear un nuevo producto
@product_bp.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        if not data.get('name') or not data.get('price') or not data.get('stock'):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        new_product = {
            "name": data['name'],
            "price": data['price'],
            "category": data.get('category', None),
            "stock": data['stock']
        }

        result = current_app.db.products.insert_one(new_product)
        new_product['_id'] = str(result.inserted_id)

        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT: Actualizar un producto existente
@product_bp.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        
        # Verificar si todos los campos necesarios están presentes
        required_fields = ["name", "price", "category", "stock"]
        missing_fields = [field for field in required_fields if field not in data or data[field] is None]

        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
        
        # Crear el diccionario con los datos actualizados
        updated_data = {
            "name": data["name"],
            "price": data["price"],
            "category": data["category"],
            "stock": data["stock"]
        }

        # Actualizar el producto en la base de datos
        result = current_app.db.products.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": updated_data}
        )

        if result.matched_count == 0:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify({'message': 'Product updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE: Eliminar un producto
@product_bp.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        result = current_app.db.products.delete_one({"_id": ObjectId(product_id)})
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Product not found'}), 404

        return jsonify({'message': 'Product deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500
