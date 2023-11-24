import mysql.connector
def validar_paciente():
    """Esta función permite buscar a un paciente en la base de datos por su número de identificación
    para validar su existencia y que pueda acceder las operaciones correspondientes.
    INPUTS:
    -Número de Identificación.
    """
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
            id_paciente = input("""Ingrese su número de identificación:
            (Presiona 0 para salir)
            >""")

            # Consulta para verificar si el paciente existe
            consulta_verificar = "SELECT * FROM pacientes WHERE cedula = %s"
            cursor.execute(consulta_verificar, (id_paciente,))
            paciente = cursor.fetchone()
            if id_paciente=="0":
                return False
            if paciente:
                return True
            else:
                print("No se encontró un paciente con ese ID.")
                continue   

        except mysql.connector.Error as error:
            print("Error al actualizar información del paciente:", error)
            continue

# validar_paciente()

def validar_medico():
    """Esta función permite buscar a un médico en la base de datos por su número de identificación
    para validar su existencia y que pueda acceder las operaciones correspondientes.
    INPUTS:
    -Número de Identificación."""
     
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
            id_medico = input("""Ingrese su número de identificación: 
            (Presiona 0 para salir)
            >""")
            # Consulta para verificar si el paciente existe
            consulta_verificar = "SELECT * FROM medicos WHERE cedula = %s"
            cursor.execute(consulta_verificar, (id_medico,))
            medico = cursor.fetchone()
            if id_medico=="0":
                return False
            if medico:
                return True
            else:
                print("No se encontró un médico con ese ID.")
                continue
        except mysql.connector.Error as error:
            print("Error al actualizar información del paciente:", error)
            continue
# buscar_medico()