import mysql.connector

def mostrar_pacientes():
    """Esta función muestra los pacientes registrados y sus ID's para buscar las citas médicas asociadas.
    """
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

        # Consulta para obtener los IDs de los pacientes
        consulta_pacientes = "SELECT id, nombre FROM pacientes"
        cursor.execute(consulta_pacientes)
        pacientes = cursor.fetchall()

        if pacientes:
            print("Pacientes disponibles:")
            for paciente in pacientes:
                print(f"ID: {paciente[0]}, Nombre: {paciente[1]}")
            return pacientes
        else:
            print("No hay pacientes disponibles.")
            return None

       

    except mysql.connector.Error as error:
        print("Error al obtener lista de pacientes:", error)
        return None 
    # Cerrar el cursor y la conexión
    # cursor.close()
    # conexion.close()

def revisar_citas_paciente():
    """Esta función permite revisar las citas asociadas al paciente seleccionado en
    la función (mostrar_pacientes).
    INPUTS:
    -ID del paciente del que se realizará la busqueda de citas.
    OUTPUTS:
    -Información de las citas asociadas al paciente seleccionado."""
    try:
        # Mostrar pacientes disponibles
        pacientes = mostrar_pacientes()
        while True:
            if pacientes:
            # Solicitar al usuario seleccionar un paciente por ID
                while True:
                    id_seleccionado = input("""Ingrese el ID del paciente para revisar sus citas: 
                    (Presione 0 para salir)
                    >""")

                    # Verificar si el ID ingresado corresponde a un paciente existente
                    paciente_seleccionado = next((paciente for paciente in pacientes if str(paciente[0]) == id_seleccionado), None)

                    if paciente_seleccionado:
                        # Establecer la conexión a la base de datos
                        conexion = mysql.connector.connect(
                            host="localhost",
                            user="informatica1",
                            password="bio123",
                            database="informatica1"
                        )

                        # Crear un cursor para ejecutar consultas
                        cursor = conexion.cursor()

                        # Consulta para obtener las citas del paciente seleccionado con los nombres de los médicos
                        consulta_citas = (
                            "SELECT c.id, c.fecha,c.hora, m.nombre "
                            "FROM citas c "
                            "JOIN medicos m ON c.id_medico = m.id "
                            "WHERE c.id_paciente = %s"
                        )
                        cursor.execute(consulta_citas, (id_seleccionado,))
                        citas = cursor.fetchall()

                        if citas:
                            print("Citas programadas para el paciente:")
                            for cita in citas:
                                print(f" Fecha: {cita[1]},Hora:{cita[2]} Médico: {cita[3]}")
                            continue
                        elif id_seleccionado==0:
                            break
                        else:
                            print("El paciente no tiene citas programadas.")
                            continue
                    break
            
            else:
                print("ID de paciente no válido.")
                continue
            break
    except mysql.connector.Error as error:
        print("Error al revisar citas:", error)
        # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()


# revisar_citas_paciente()

