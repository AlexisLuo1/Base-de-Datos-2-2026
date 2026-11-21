# Sistema de Expedientes

## Cómo ejecutar el proyecto

### 1. Abrir Docker
Abrir Docker Desktop y esperar a que inicie.

### 2. Abrir la carpeta del proyecto
Abrir la carpeta del proyecto en Visual Studio Code y abrir una terminal.

### 3. Crear el entorno virtual
Ejecutar:
python -m venv .venv

### 4. Activar el entorno virtual
Ejecutar:
.venv\Scripts\activate

### 5. Instalar las librerías
Ejecutar:
pip install -r requirements.txt

### 6. Iniciar la base de datos
Ejecutar:
docker compose up -d

### 7. Crear las tablas
Abrir MySQL Workbench y conectarse con:
Host: 127.0.0.1
Puerto: 3308
Usuario: root
Contraseña: 12345

Ejecutar el archivo:
schema.sql

### 8. Crear el usuario
Ejecutar:
python crear_usuario.py

Escribir el usuario y la contraseña que se utilizarán para iniciar sesión.

### 9. Agregar datos de ejemplo
Ejecutar:
python datos_ejemplo.py

### 10. Iniciar el programa
Ejecutar:
python main.py

### 11. Abrir la página
Abrir en el navegador:
http://127.0.0.1:5000

### API REST
Para ver los expedientes en formato JSON:
http://127.0.0.1:5000/api/expedientes

