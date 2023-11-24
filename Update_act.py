import mysql.connector

def actualizar_paciente():
    """Esta función muestra los pacientes registrados, permite actualizar 
    sus datos  y actualizarlos en la base de datos.
    
    INPUTS:
    -ID.(Seleccionar el paciente.)
    [Datos modificables]
    -Telefono.
    -Dirección.
    -Correo electrónico.
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

        # Consulta para obtener los pacientes disponibles para actualizar
        consulta_pacientes = "SELECT id, nombre FROM pacientes"
        cursor.execute(consulta_pacientes)
        pacientes = cursor.fetchall()

        if pacientes:
            print("Pacientes disponibles para actualizar:")
            for paciente in pacientes:
                print(f"{paciente[0]} - {paciente[1]}")
            while True:
                # Obtener el ID del paciente que se desea actualizar
                id_paciente = input("""Ingrese el ID del paciente que desea actualizar: 
                (Presiona 0 para salir)
                >""")
                if id_paciente=="0":
                    break
                # Consulta para verificar si el paciente existe
                consulta_verificar = "SELECT * FROM pacientes WHERE id = %s"
                cursor.execute(consulta_verificar, (id_paciente,))
                paciente = cursor.fetchone()

                if paciente:
                    # Solicitar los nuevos datos del paciente al usuario
                    print("Ingrese los datos a actualizar del paciente:")
                    
                    while True:
                        n_telefono = input("Ingrese el número de teléfono del paciente: ") 
                        try:
                            tel1=int(n_telefono)
                            if len(n_telefono)!=10:
                                print("La cantidad de dígitos del número de telefono debe ser de 10. ")
                                continue
                            break
                        except ValueError:
                            print("Ingrese valores numericos.")
                            continue
                    
                    n_direccion = input("Ingrese la dirección del paciente: ").title()
                    n_email = input("Ingrese el correo electrónico: ")


                    # Consulta para actualizar la información del paciente en la base de datos
                    consulta_actualizar = "UPDATE pacientes SET telefono=%s, direccion= %s,email=%s WHERE id = %s"
                    datos_actualizados = ( n_telefono, n_direccion, n_email, id_paciente)

                    # Ejecutar la consulta SQL
                    cursor.execute(consulta_actualizar, datos_actualizados)

                    # Confirmar los cambios en la base de datos
                    conexion.commit()

                    print("Información del paciente actualizada correctamente.")
                    continue
                else:
                    print("No se encontró un paciente con ese ID.")
                    continue
        else:
            print("No hay pacientes disponibles para actualizar.")
    
             
    except mysql.connector.Error as error:
        print("Error al actualizar información del paciente:", error)
 # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

# actualizar_paciente()



import mysql.connector

def actualizar_medico():
    """Esta función muestra los medicos registrados, permite actualizar sus datos  y 
    actualizarlos en la base de datos.
    INPUTS:
    -ID.(Seleccionar el paciente.)
    [Datos modificables]
    -Telefono.
    -Correo electrónico.
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

        # Consulta para obtener los médicos disponibles para actualizar
        consulta_medicos = "SELECT id, nombre FROM medicos"
        cursor.execute(consulta_medicos)
        medicos = cursor.fetchall()

        if medicos:
            print("Médicos disponibles para actualizar:")
            for medico in medicos:
                print(f"{medico[0]} - {medico[1]}")

            # Obtener el ID del médico que se desea actualizar
            while True:
                id_medico = input("""Ingrese la ID del médico que desea actualizar: 
                (Presiona 0 para salir)
                >""")
                if id_medico=="0":
                    break

                # Consulta para verificar si el médico existe
                consulta_verificar = "SELECT * FROM medicos WHERE id = %s"
                cursor.execute(consulta_verificar, (id_medico,))
                medico = cursor.fetchone()

                if medico:
                    # Solicitar los nuevos datos del médico al usuario
                    print("Ingrese los datos a actualizar del médico :")
                    while True:
                        n_telefono = input("Ingrese el número de teléfono del médico: ") 
                        try:
                            tel1=int(n_telefono)
                            if len(n_telefono)!=10:
                                print("La cantidad de dígitos del número de telefono debe ser de 10. ")
                                continue
                            break
                        except ValueError:
                            print("Ingrese valores numericos.")
                            continue
                    n_email = input("Ingrese el correo electrónico del médico: ")
                        # Consulta para actualizar la información del médico en la base de datos
                    consulta_actualizar = "UPDATE medicos SET telefono=%s,email=%s WHERE id = %s"
                    datos_actualizados = ( n_telefono, n_email, id_medico)

                    # Ejecutar la consulta SQL
                    cursor.execute(consulta_actualizar, datos_actualizados)

                    # Confirmar los cambios en la base de datos
                    conexion.commit()

                    print("Información del médico actualizada correctamente.")
                    continue
                else:
                    print("No se encontró un médico con ese ID.")
                    continue
            
        else:
            print("No hay médicos disponibles para actualizar.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print("Error al actualizar información del médico:", error)


# actualizar_medico()
