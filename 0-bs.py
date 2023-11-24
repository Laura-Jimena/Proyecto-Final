import mysql.connector

conexion= mysql.connector.connect(
    host="localhost",
    user="informatica1",
    password="bio123",
    port="3306",
    database="informatica1"

)

# Crear el cursor para ejecutar consultas
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        cedula VARCHAR(255),
        fecha_nacimiento DATE,
        genero VARCHAR(10),
        tipo_sangre VARCHAR(10),
        telefono VARCHAR(20),
        direccion VARCHAR(255),
        email VARCHAR(255)
    )
""")

#  Crear la tabla de médicos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        cedula VARCHAR(100),
        especialidad VARCHAR(255),
        telefono VARCHAR(20),
        email VARCHAR(255)
    )
""")

# # Crear la tabla de citas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_paciente INT,
        id_medico INT,
        fecha DATE,
        hora TIME,
        estado VARCHAR(20),
        FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
        FOREIGN KEY (id_medico) REFERENCES medicos(id)
    )
""")

# Crear la tabla de disponibilidad
cursor.execute("""
    CREATE TABLE IF NOT EXISTS disponibilidad_medicos (
        id_disponibilidad INT AUTO_INCREMENT PRIMARY KEY,
        id_medico INT,
        fecha_disponible DATE,
        hora TIME,
        FOREIGN KEY (id_medico) REFERENCES medicos(id)
    )
""")



#Confirmar los cambios en la base de datos
conexion.commit()
conexion.close()


