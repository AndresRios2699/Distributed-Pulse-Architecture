import socket
import json
import time
import random

def run_sensor(sensor_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print(f"[NODO {sensor_id}] Conectado al servidor.")

    try:
        while True:
            payload = {
                "sensor_id": sensor_id,
                "lectura": round(random.uniform(20.0, 30.0), 2)
            }
            client.send(json.dumps(payload).encode('utf-8'))
            time.sleep(3)
    except KeyboardInterrupt:
        client.close()

if __name__ == "__main__":
    name = input("Nombre de este sensor: ")
    run_sensor(name)