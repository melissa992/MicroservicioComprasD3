# Usar una imagen base de Python
FROM python:3.12.6

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y el código de la aplicación
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
