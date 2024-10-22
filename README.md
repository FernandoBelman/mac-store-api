# Mac Store API

Esta es una API para gestionar productos de una tienda de Apple. Permite realizar operaciones CRUD sobre productos, con soporte para paginación, filtrado, y cache mediante Redis.

## Requisitos

- Docker
- Docker Compose
- Python

## Configuración e instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/FernandoBelman/mac-store-api.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd mac_store_api
    ```

3. **Crea y activa un entorno virtual de Python** (opcional pero recomendado):

    - En sistemas macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - En sistemas Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

4. Instala las dependencias de Python dentro del entorno virtual:

    ```bash
    pip install -r requirements.txt
    ```

5. **Construye los contenedores de Docker**:

    ```bash
    docker-compose up --build
    ```

   Esto levantará los contenedores para la API, MongoDB, y Redis.

6. Accede a la documentación de la API (Swagger) en tu navegador:

    ```
    http://localhost:5000/api/docs
    ```

## Endpoints

- `POST /api/products`: Crear un nuevo producto.
- `GET /api/products`: Obtener productos con soporte para paginación y filtro.
    - Parámetros:
        - `page`: Número de página.
        - `page_size`: Tamaño de la página.
        - `field`: Campo por el cual filtrar.
        - `value`: Valor para el filtro.
- `GET /api/products/<product_id>`: Obtener un producto por su ID.
- `PUT /api/products/<product_id>`: Actualizar un producto completo.
- `PATCH /api/products/<product_id>`: Actualizar propiedades específicas de un producto.
- `DELETE /api/products/<product_id>`: Eliminar un producto.