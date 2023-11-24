import mysql.connector
def buscar_paciente():
    """Esta función permite buscar a un paciente en la base de datos por su número de identificación.
    INPUTS:
    -Número de Identificación.
    OUTPUTS:
    -Información asociada al paciente."""
    while True:
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
                    # Obtener el ID del paciente que se desea actualizar
                id_paciente = input("""Ingrese el número de identificación del paciente que desea actualizar: 
                (Presiona 0 para salir)
                >""")

                # Consulta para verificar si el paciente existe
                consulta_verificar = "SELECT * FROM pacientes WHERE cedula = %s"
                cursor.execute(consulta_verificar, (id_paciente,))
                paciente = cursor.fetchone()
                if id_paciente=="0":
                    break
                if paciente:
                    print(paciente)
                    continue
                else:
                    print("No se encontró un paciente con ese ID.")
                    confirm=input()
                    continue  
        except mysql.connector.Error as error:
            print("Error al actualizar información del paciente:", error)
            continue


def buscar_medico():
    """Esta función permite buscar a un médico en la base de datos por su número de identificación.
    INPUTS:
    -Número de Identificación.
    OUTPUTS:
    -Información asociada al médico."""
     
    while True:
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
            
            # Obtener el documeto del medico que se desea actualizar
            id_medico = input("""Ingrese el número de identificación del medico que desea actualizar: 
            (Presiona 0 para salir)
            >""")
            if id_medico=="0":
                break
            # Consulta para verificar si el paciente existe
            consulta_verificar = "SELECT * FROM medicos WHERE cedula = %s"
            cursor.execute(consulta_verificar, (id_medico,))
            medico = cursor.fetchone()
            if id_medico=="0":
                break
            if medico:
                print(medico)
                continue
            else:
                print("No se encontró un médico con ese ID.")
                continue
        except mysql.connector.Error as error:
            print("Error al actualizar información del paciente:", error)
            continue
# buscar_medico()