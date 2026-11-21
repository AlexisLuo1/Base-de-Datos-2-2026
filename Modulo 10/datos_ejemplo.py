from conexion import conectar

conexion = conectar()
cursor = conexion.cursor()

datos = [
    ("EXP-2026-001", "Anthony Trejos", "ASSA", "Juzgado 5to", "PENDIENTE", "2026-11-12"),
    ("EXP-2026-002", "Luis Molina", "ANCON", "Juzgado 4to", "EN CURSO", "2026-11-12"),
    ("EXP-2026-003", "Katherine Kent", "ASSA", "Juzgado 5to", "CERRADO", "2026-11-13"),
    ("EXP-2026-004", "Martin Alvarado", "COMANDE", "Juzgado 1ro", "PENDIENTE", "2026-11-13"),
    ("EXP-2026-005", "Joel Rodriguez", "PARTICULAR", "Juzgado 3ro", "EN CURSO", "2026-11-16")
]

for dato in datos:

    sql = """
    INSERT INTO expedientes
    (numero, asegurado, aseguradora, juzgado, estado, fecha)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, dato)

conexion.commit()

print("Datos agregados")

conexion.close()