import mysql.connector

def eliminar_pacientes():
    """Esta función muestra los pacientes registrados y permite eliminarlo.
     INPUTS:
    -ID.(Seleccionar el paciente.)"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
        )
        cursor = conexion.cursor()

        consulta_pacientes = "SELECT id, nombre FROM pacientes"
        cursor.execute(consulta_pacientes)
        pacientes = cursor.fetchall()

        if pacientes:
            print("Opciones de pacientes disponibles:")
            for paciente in pacientes:
                print(f"{paciente[0]} - {paciente[1]}")
            while True:
                paciente_seleccionado = input("""Ingrese el ID del paciente a eliminar:
                (Presiona 0 para salir)
                >""")
                if paciente_seleccionado=="0":
                    break

                consulta_eliminar_paciente = "DELETE FROM pacientes WHERE id = %s"
                cursor.execute(consulta_eliminar_paciente, (paciente_seleccionado,))
                conexion.commit()

                print("Paciente eliminado correctamente.")
                continue

        else:
            print("No hay pacientes disponibles.")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print("Error al eliminar paciente:", error)

# eliminar_pacientes()


def eliminar_medico_con_citas():
    """Esta función muestra los médicos registrados y permite eliminarlo.
     INPUTS:
    -ID.(Seleccionar el médico.)"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
        )
        cursor = conexion.cursor()

        # Mostrar médicos disponibles para elegir cuál eliminar
        consulta_medicos = "SELECT id, nombre FROM medicos"
        cursor.execute(consulta_medicos)
        medicos = cursor.fetchall()

        if medicos:
            print("Médicos disponibles para eliminar:")
            for medico in medicos:
                print(f"{medico[0]} - {medico[1]}")
            
            while True:
                id_medico = input("""Ingrese el ID del médico a eliminar:
                 (Presiona 0 para salir)
                >""")
                if id_medico=="0":
                    break   

                # Eliminar las citas del médico
                consulta_eliminar_citas = "DELETE FROM citas WHERE id_medico = %s"
                cursor.execute(consulta_eliminar_citas, (id_medico,))
                conexion.commit()

                # Eliminar la disponibilidad del médico
                consulta_eliminar_disponibilidad = "DELETE FROM disponibilidad_medicos WHERE id_medico = %s"
                cursor.execute(consulta_eliminar_disponibilidad, (id_medico,))
                conexion.commit()

                # Luego eliminar al médico
                consulta_eliminar_medico = "DELETE FROM medicos WHERE id = %s"
                cursor.execute(consulta_eliminar_medico, (id_medico,))
                conexion.commit()

                print("Médico y sus citas eliminados correctamente.")
                continue
        else:
            print("No hay médicos disponibles para eliminar.")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print("Error al eliminar médico y citas:", error)

# eliminar_medico_con_citas()




