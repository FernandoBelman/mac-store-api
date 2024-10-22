import os
from flask import Flask, send_from_directory
from app import create_app
from flask_swagger_ui import get_swaggerui_blueprint

app = create_app()

# Configuración de Swagger
SWAGGER_URL = '/api/docs'  # URL donde se encontrará Swagger UI
API_URL = '/swagger.json'  # URL para acceder al archivo swagger.json

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Mac Store API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Sirviendo el archivo swagger.json desde el directorio raíz
@app.route('/swagger.json')
def swagger_file():
    return send_from_directory(os.path.abspath("."), 'swagger.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
