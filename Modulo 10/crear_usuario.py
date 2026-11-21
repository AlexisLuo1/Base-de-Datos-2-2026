from conexion import conectar

conexion = conectar()
cursor = conexion.cursor()

usuario = input("Usuario: ")
clave = input("Contraseña: ")

sql = "INSERT INTO usuarios (usuario, clave) VALUES (?, ?)"

cursor.execute(sql, (usuario, clave))

conexion.commit()

print("Usuario creado")

conexion.close()