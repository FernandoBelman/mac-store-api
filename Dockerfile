# Usa una imagen base de Python
FROM python:3.11.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .
COPY . /app/static

# Expone el puerto en el que Flask estará corriendo
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "-m", "app.main"]

