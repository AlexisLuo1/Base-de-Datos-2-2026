USE bd_clase;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    clave VARCHAR(50)
);

CREATE TABLE expedientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(50),
    asegurado VARCHAR(100),
    aseguradora VARCHAR(100),
    juzgado VARCHAR(100),
    estado VARCHAR(30),
    fecha DATE
);