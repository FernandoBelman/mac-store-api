from app.controllers.product_controller import *
from app.repositories.product_repository import *
from app.models.product_model import Product
from app.cache import cache_get, cache_set



def get_product(id):

    cached = cache_get(id)
    if cached:
        return cached
    product = get_product_by_id(id)
    if product:
        cache_set(id, product)
        return product
    
def get_paginated_products(page, page_size):
    key = f"products:{page}:{page_size}"
    cached = cache_get(key)
    if cached:
        return cached
    products = get_products(page, page_size)
    cache_set(key,products)
    return products

def create_product(data):
    product = Product(**data)
    return add_product(product.to_dict())