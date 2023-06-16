import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
with open('modelo_entrenado.pkl', 'rb') as file:
    trained_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos enviados en la solicitud POST
    data = request.get_json()
    
    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(data)
    
    # Realizar las predicciones utilizando el modelo entrenado
    predictions = trained_model.predict(df)
    
    # Devolver las predicciones en formato JSON
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run()
