# Usa una imagen base adecuada
FROM python:3.9

# Establece el directorio de trabajo en la carpeta de la aplicación
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY app.py /app
COPY modelo_entrenado.pkl /app
COPY requirements.txt /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
