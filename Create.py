import mysql.connector
# conexion = mysql.connector.connect(
#     host="localhost",
#     user="informatica1",
#     password="bio123",
#     database="informatica1"
#     )
from EspecialFunc import*

# Función para ingresar pacientes a la base de datos
def ingresar_paciente():
    """Esta función permite crear un nuevo paciente y añadir los datos asociados a este a la base de datos.
    INPUTS:
    -Nombre.
    -Identificación.
    -Fecha de nacimiento.
    -Genero.
    -Tipo de sangre.
    -Telefono.
    -Dirección.
    -Correo electrónico.
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

            # Solicitar los datos del paciente al usuario
            print("Ingrese los datos del nuevo paciente:")
            nombre = input("""Ingrese el nombres y appellidos del paciente:
            (Presiona 0 para salir) 
            >""").title()
            if nombre=="0": 
                break
            while True:
                cedula= input("Ingrese el número de Identificación del paciente:") 
                try:
                    cedula1=int(cedula)
                    if 7>len(cedula) or len(cedula)>11:
                        print("La cantidad de dígitos del número de identificación está fuera del rango de 7 a 11. ")
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
            print("[Fecha de Nacimiento del paciente:]")
            while True:
                ano=input("Ingrese el año: ")
                try:
                    ano1=int(ano)
                    if len(ano)!=4:
                        print("El año debe tener 4 dígitos.")
                        continue
                    if validar_anonac(ano1)==True:
                        break
                    elif validar_anonac(ano1)==False:
                        print("Año invalido, ingrese año actual o pasado.")
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
            while True:
                mes=input("Ingrese el mes: ")
                try:
                    mes1=int(mes)
                    if len(mes)!=2:
                        print("El mes debe tener 2 dígitos.")
                        continue
                    elif mes1>12 or mes1==0:
                        print("Mes invalido, ingrese mes actual o pasado.")
                        continue
                    if validar_mesnac(mes1,ano1)==True:
                        break
                    if validar_mesnac(mes1,ano1)==False:
                        continue
                    break

                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
            
            while True:
                dia=input("Ingrese el día: ")
                try:
                    dia1=int(dia)
                    if len(dia)!=2:
                        print("El día debe tener 2 dígitos.")
                        continue
                    elif mes1==2 and dia1>28:
                        print("Dia invalido, ingrese día actual o pasado.")
                        continue
                    elif dia1>31:
                        print("Dia invalido, ingrese día actual o pasado.")
                        continue
                    elif mes1==4 or mes1==6 or mes1==9 or mes1==11  and dia1>30:
                        print("Dia invalido, ingrese día actual o pasado.")
                        continue

                    elif dia1>31 or dia1==0:
                        print("Dia invalido, ingrese día actual o pasado.")
                        continue
                    if validar_dianac(dia1,mes1,ano1)==True:
                        break
                    if validar_dianac(dia1,mes1,ano1)==False:
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
                
            fecha_nacimiento = f"{ano}/{mes}/{dia}"
            genero = input("Ingrese el género del paciente: ").capitalize()
            tipo_sangre = input("Ingrese el tipo de sangre del paciente: ").upper()
            while True:
                telefono = input("Ingrese el número de teléfono del paciente: ") 
                try:
                    tel1=int(telefono)
                    if len(telefono)!=10:
                        print("La cantidad de dígitos del número de telefono debe ser de 10. ")
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
                
            direccion = input("Ingrese la dirección del paciente: ").title()        
            email = input("Ingrese el correo electrónico del paciente: ")

                # Consulta para insertar un paciente en la base de datos
            consulta ="INSERT INTO pacientes (nombre,cedula, fecha_nacimiento, genero, tipo_sangre, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
            datos_paciente=(nombre,cedula, fecha_nacimiento, genero, tipo_sangre, telefono, direccion, email)
            

            # Ejecutar la consulta SQL
            cursor.execute(consulta, datos_paciente)

            # Confirmar los cambios en la base de datos
            conexion.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            conexion.close()

            print("Paciente ingresado correctamente a la base de datos.")
            continue

        except mysql.connector.Error as error:
            print("Error al ingresar paciente a la base de datos:", error)
            continue
           
# ingresar_paciente()



#Funcion para ingresar Medico
def ingresar_medico():
    """Esta función permite crear un nuevo médico y añadir los datos asociados a este a la base de datos.
    INPUTS:
    -Nombre.
    -Identificación.
    -Especialidad médica.
    -Telefono.
    -Correo electrónico.
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

            # Solicitar los datos del paciente al usuario
            print("Ingrese los datos del medico:")
            nombre = input("""Ingrese el nombres y apellidos del médico:
            (Presiona 0 para salir)
            >""").title()
            if nombre=="0":
                break
            while True:
                cedula= input("Ingrese el número de Identificación del médico:") 
                try:
                    cedula1=int(cedula)
                    if 7>len(cedula) or len(cedula)>11:
                        print("La cantidad de dígitos del número de identificación está fuera del rango de 7 a 11. ")
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
            esp_medica = input("Ingrese la especialidad medica: ").upper()
            while True:
                telefono = input("Ingrese el número de teléfono del médico: ") 
                try:
                    tel1=int(telefono)
                    if len(telefono)!=10:
                        print("La cantidad de dígitos del número de telefono debe ser de 10. ")
                        continue
                    break
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
            email = input("Ingrese el correo electrónico del médico: ")

            # Consulta para insertar un paciente en la base de datos
            consulta ="INSERT INTO medicos (nombre,cedula,especialidad,telefono,email) VALUES (%s, %s, %s, %s,%s)"
            datos_medico=(nombre,cedula, esp_medica, telefono, email)
            

            # Ejecutar la consulta SQL
            cursor.execute(consulta, datos_medico)

            # Confirmar los cambios en la base de datos
            conexion.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            conexion.close()

            print(f"Medico {nombre} ingresado correctamente a la base de datos.")
            continue

        except mysql.connector.Error as error:
            print("Error al ingresar medico a la base de datos:", error)
            continue

# ingresar_medico()

