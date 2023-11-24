import mysql.connector

# Función para mostrar opciones de médicos disponibles
def mostrar_medicos(cursor):
    """Esta función muestra los médicos disponibles con sus ID's para asignar las citas y 
    elegir el médico.
    INPUTS:
    -Seleccionar el ID del médico. """
    try:
        consulta_medicos = "SELECT id, nombre FROM medicos"
        cursor.execute(consulta_medicos)
        medicos = cursor.fetchall()

        if medicos:
            print("Opciones de médicos disponibles:")
            for medico in medicos:
                print(f"{medico[0]} - {medico[1]}")
            
            while True:
                medico_seleccionado = input("Ingrese el ID del médico seleccionado: ")
                if any(medico_seleccionado == str(medico[0]) for medico in medicos):
                    return medico_seleccionado
                else:
                    print("ID de médico no válido. Intente nuevamente.")
        else:
            print("No hay médicos disponibles.")
            return None
    except mysql.connector.Error as error:
        print("Error al obtener la lista de médicos:", error)
        return None

# Función para mostrar opciones de pacientes disponibles
def mostrar_pacientes(cursor):
    """Esta función muestra los pacientes con sus ID's a lo que se les van a programar las citas y elegir
    el paciente.
    INPUTS:
    -Seleccionar el ID del Paciente."""
    try:
        consulta_pacientes = "SELECT id, nombre FROM pacientes"
        cursor.execute(consulta_pacientes)
        pacientes = cursor.fetchall()

        if pacientes:
            print("Opciones de pacientes disponibles:")
            for paciente in pacientes:
                print(f"{paciente[0]} - {paciente[1]}")
            
            while True:
                paciente_seleccionado = input("Ingrese el ID del paciente seleccionado: ")
                if any(paciente_seleccionado == str(paciente[0]) for paciente in pacientes):
                    return paciente_seleccionado
                else:
                    print("ID de paciente no válido. Intente nuevamente.")
        else:
            print("No hay pacientes disponibles.")
            return None
    except mysql.connector.Error as error:
        print("Error al obtener la lista de pacientes:", error)
        return None



def mostrar_fechas(cursor, medico):
    """Esta función muestra las disponibilidades de cada médico.
    INPUTS:
    -Seleccionar el ID de la disponibilidad. """
    try:
        datos_medicos = (medico,)
        consulta_fechas = "SELECT id_disponibilidad, fecha_disponible, hora FROM disponibilidad_medicos WHERE id_medico = %s"
        cursor.execute(consulta_fechas, datos_medicos)
        fechas = cursor.fetchall()
        
        if fechas:
            print("Opciones de fechas y horas disponibles para citas:")
            for fecha in fechas:
                print(f"{fecha[0]} - Fecha: {fecha[1]}, Hora: {fecha[2]}")  # Modificación en la impresión
            
            while True:
                fecha_seleccionada = input("Ingrese el ID de la fecha para la cita: ")
                if any(fecha_seleccionada == str(fecha[0]) for fecha in fechas):
                    return fecha_seleccionada
                else:
                    print("ID de fecha no válido. Intente nuevamente.")
        else:
            print("No hay fechas disponibles para citas.")
            return None
    except mysql.connector.Error as error:
        print("Error al obtener la lista de fechas:", error)
        return None




def programar_cita():
    """Esta función permite programar las citas.
    INPUTS:
    -ID del médico.
    -ID del paciente.
    -ID de la fecha disponible.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
        )
        cursor = conexion.cursor()
        while True:
            id_medico = mostrar_medicos(cursor)
            if id_medico:
                id_paciente = mostrar_pacientes(cursor)
                if id_paciente:
                    id_fecha = mostrar_fechas(cursor, id_medico)  # Se utiliza la función actualizada aquí
                    if id_fecha:
                        consulta_obtener_fecha_medico = "SELECT id_medico, fecha_disponible, hora FROM disponibilidad_medicos WHERE id_disponibilidad = %s"
                        cursor.execute(consulta_obtener_fecha_medico, (id_fecha,))
                        datos_fecha = cursor.fetchone()
                        if datos_fecha:
                            id_medico = datos_fecha[0]
                            fecha = datos_fecha[1]
                            hora = datos_fecha[2]

                            consulta_programar_cita = "INSERT INTO citas (id_paciente, id_medico, fecha, hora) VALUES (%s, %s, %s, %s)"
                            datos_cita = (id_paciente, id_medico, fecha, hora)
                            cursor.execute(consulta_programar_cita, datos_cita)

                            consulta_eliminar = "DELETE FROM disponibilidad_medicos WHERE id_disponibilidad = %s"
                            cursor.execute(consulta_eliminar, (id_fecha,))

                            conexion.commit()
                            print("Cita programada correctamente.")
                            break
                else:
                    continue

            cursor.close()
            conexion.close()

    except mysql.connector.Error as error:
        print("Error al programar la cita:", error)

# programar_cita()
