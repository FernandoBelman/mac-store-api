from flask import Blueprint, jsonify, request
from app.services.product_service import *

product_bp = Blueprint('product_bp', __name__)

# GET para obtener múltiples productos con paginación
@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        field = request.args.get('field', None)
        value = request.args.get('value', None)
        
        products = get_paginated_products(page, page_size, field, value)
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET para obtener un producto por ID
@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = get_product_by_id_service(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST para crear un nuevo producto
@product_bp.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        if not data.get('name') or not data.get('price') or not data.get('stock'):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        product = create_product(data)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT para actualizar un producto completo
@product_bp.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        updated, error = update_product_service(product_id, data)
        if error:
            return jsonify({'error': error}), 400
        if not updated:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'message': 'Product updated successfully'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PATCH para actualizar parcialmente un producto
@product_bp.route('/products/<product_id>', methods=['PATCH'])
def patch_product(product_id):
    try:
        data = request.get_json()
        updated, error = update_partial_product_service(product_id, data)
        if error:
            return jsonify({'error': error}), 400
        if not updated:
            return jsonify({'error': 'Product not found'}), 404
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE para eliminar un producto
@product_bp.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        deleted = delete_product_service(product_id)
        if not deleted:
            return jsonify({'error': 'Product not found'}), 404
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500
