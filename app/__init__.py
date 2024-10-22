from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config
from app.controllers.product_controller import product_bp

mongo = PyMongo()  # Inicializa PyMongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)  # Inicializa Mongo con la app
    app.db = mongo.db  # Guarda la referencia de la base de datos

    # Registrar Blueprints
    app.register_blueprint(product_bp, url_prefix='/api')
    
    return app
