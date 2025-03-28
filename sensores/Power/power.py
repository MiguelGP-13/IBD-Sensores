import json
import random
import time    
import requests
import os 

# Obtener el índice del sensor a partir del hostname del contenedor
SENSOR_ID = os.getenv("HOSTNAME")

def generate_power_data():
    """Genera datos simulados de consumo de energía."""
    data = {
        "id": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "power_consumption": round(random.uniform(0.1, 10.0), 2),  # kWh
        "voltage": round(random.uniform(210, 240), 2),  # V
        "current": round(random.uniform(0.5, 15.0), 2),  # A
        "power_factor": round(random.uniform(0.5, 1.0), 2)  # Factor de potencia (0-1)  
    }
    return data

API_URL = "http://api-gateway:8080/consumo"  # Endpoint de la API de destino

if __name__ == "__main__":
    while True:
        power_data = generate_power_data()

        try:
            response = requests.post(API_URL, json=power_data) #se puede añadir un timeout
            response.raise_for_status()  # Lanza un error si el código de respuesta es un error
            print(json.dumps(power_data)) # Devuelve el JSON en la salida estándar
        except requests.exceptions.RequestException as e:
            print(f" Error al enviar los datos: {e}")

        time.sleep(5)  # Espera 5 segundos antes de la siguiente medición

