import socket
import threading
import json

def handle_client(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message: break
            
            # --- PATRÓN PROXY (Validación) ---
            data = json.loads(message)
            if "sensor_id" in data and "lectura" in data:
                print(f"[{data['sensor_id']}] Recibido: {data['lectura']}°C")
                # Aquí actuaría el PATRÓN OBSERVER notificando al dashboard
            else:
                print("[ERROR] Datos inválidos filtrados por el Proxy.")
        except:
            break
    conn.close()
    print(f"[DESCONECTADO] {addr} se ha ido.")

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()
    print("[SERVIDOR] Iniciado. Esperando nodos en puerto 5000...")
    while True:
        conn, addr = server.accept()
        # --- ROBUSTEZ: Manejo de Hilos ---
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[HILOS ACTIVOS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start()