from flask import Flask, render_template, request, redirect, session, jsonify
from conexion import conectar

app = Flask(__name__)

app.secret_key = "12345"


@app.route("/", methods=["GET", "POST"])
def login():

    mensaje = ""

    if request.method == "POST":

        usuario = request.form["usuario"]
        clave = request.form["clave"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM usuarios WHERE usuario=? AND clave=?"

        cursor.execute(sql, (usuario, clave))

        resultado = cursor.fetchone()

        conexion.close()

        if resultado:
            session["usuario"] = usuario
            return redirect("/inicio")
        else:
            mensaje = "Usuario o contraseña incorrecta"

    return render_template("login.html", mensaje=mensaje)


@app.route("/inicio")
def inicio():

    if "usuario" not in session:
        return redirect("/")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM expedientes")

    expedientes = cursor.fetchall()

    conexion.close()

    return render_template(
        "inicio.html",
        expedientes=expedientes,
        usuario=session["usuario"]
    )


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        numero = request.form["numero"]
        asegurado = request.form["asegurado"]
        aseguradora = request.form["aseguradora"]
        juzgado = request.form["juzgado"]
        estado = request.form["estado"]
        fecha = request.form["fecha"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO expedientes
        (numero, asegurado, aseguradora, juzgado, estado, fecha)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (numero, asegurado, aseguradora, juzgado, estado, fecha)
        )

        conexion.commit()
        conexion.close()

        return redirect("/inicio")

    return render_template("nuevo.html")


@app.route("/salir")
def salir():

    session.clear()

    return redirect("/")


@app.route("/api/expedientes", methods=["GET"])
def consultar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM expedientes")

    datos = cursor.fetchall()

    conexion.close()

    return jsonify(datos)


@app.route("/api/expedientes", methods=["POST"])
def insertar():

    datos = request.get_json()

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO expedientes
    (numero, asegurado, aseguradora, juzgado, estado, fecha)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, (
        datos["numero"],
        datos["asegurado"],
        datos["aseguradora"],
        datos["juzgado"],
        datos["estado"],
        datos["fecha"]
    ))

    conexion.commit()
    conexion.close()

    return "Expediente agregado"


@app.route("/api/expedientes/<int:id>", methods=["PUT"])
def editar(id):

    datos = request.get_json()

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    UPDATE expedientes
    SET numero=?, asegurado=?, aseguradora=?,
    juzgado=?, estado=?, fecha=?
    WHERE id=?
    """

    cursor.execute(sql, (
        datos["numero"],
        datos["asegurado"],
        datos["aseguradora"],
        datos["juzgado"],
        datos["estado"],
        datos["fecha"],
        id
    ))

    conexion.commit()
    conexion.close()

    return "Expediente editado"


@app.route("/api/expedientes/<int:id>", methods=["DELETE"])
def eliminar(id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM expedientes WHERE id=?",
        (id,)
    )

    conexion.commit()
    conexion.close()

    return "Expediente eliminado"


app.run(debug=True)