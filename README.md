# Distributed-Pulse-Architecture
Sistema distribuido multihilo en Python para monitoreo de sensores IoT
# Distributed Pulse - Arquitectura Distribuida Multihilo

Este proyecto presenta una solución robusta para el monitoreo de datos de sensores IoT, implementando una arquitectura distribuida con gestión de hilos independientes y patrones de diseño avanzados.

## Características
- **Multithreading:** Manejo de múltiples clientes simultáneos.
- **Patrón Proxy:** Validación de integridad de datos JSON.
- **Patrón Observer:** Notificación de eventos en tiempo real.
- **Robustez:** Tolerancia a fallos y desconexiones abruptas.

##  Tecnologías
- Python 3.12
- Sockets (TCP/IP)
- JSON Serialization
- PlantUML (Modelado)

## Cómo ejecutar
1. Iniciar el servidor: `python3 server.py`
2. Iniciar uno o más sensores: `python3 sensor.py`
