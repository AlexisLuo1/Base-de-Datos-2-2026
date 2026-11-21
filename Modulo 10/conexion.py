import mariadb

def conectar():
    conexion = mariadb.connect(
        host="127.0.0.1",
        port=3308,
        user="root",
        password="12345",
        database="bd_clase"
    )

    return conexion