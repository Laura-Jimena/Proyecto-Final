import mysql.connector
import csv

def leer_infopac():
    """Esta función permite ver todos los pacientes almacenados en la base de datos en forma de tupla y 
    crear un archivo CSV que los almacene con un nombre elegido por el ususario.
    INPUTS:
    -Nombre de archivo."""

    try:
        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
            )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()
        infopac = "SELECT * FROM pacientes"

        cursor.execute(infopac)


        results = cursor.fetchall()
        name=input("Ingrese el nombre del archivo a crear:")
        namefile=f"{name}.csv"
        for i in results:
            print(i)
            with open(f"{namefile}","a",newline="") as csv_file:
                spamwriter=csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(i)
    except mysql.connector.Error as error:
        print("Error al ingresar medico a la base de datos:", error)

            
# leer_infopac()

def leer_infomed():
    """Esta función permite ver todos los médicos almacenados en la base de datos en forma de tupla y 
    crear un archivo CSV que los almacene con un nombre elegido por el ususario.
    INPUTS:
    -Nombre de archivo."""
    try:
        # Establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
            )

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()
        infomed = "SELECT * FROM medicos"

        cursor.execute(infomed)


        results = cursor.fetchall()
        name=input("Ingrese el nombre del archivo a crear:")
        namefile=f"{name}.csv"
        for i in results:
            print(i)
            with open(f"{namefile}","a",newline="") as csv_file:
                spamwriter=csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(i)
    except mysql.connector.Error as error:
        print("Error al ingresar medico a la base de datos:", error)

# leer_infomed()