import mysql.connector
from EspecialFunc import*

def mostrar_medicos():
    """Esta función permite visualizar los médicos disponibles y sus respectivos ID, y elegir
    a que medico queremos agregarle espacios de disponibilidad.
    INPUTS:
    -ID del médico."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123",
            database="informatica1"
        )
        cursor = conexion.cursor()

        consulta_medicos = "SELECT id, nombre FROM medicos"
        cursor.execute(consulta_medicos)
        medicos = cursor.fetchall()

        if medicos:
            print("Opciones de médicos disponibles:")
            for medico in medicos:
                print(f"{medico[0]} - {medico[1]}")
            while True:
                id_medico = input("Ingrese el ID del médico seleccionado: ")
                if any(id_medico == str(medico[0]) for medico in medicos):
                    cursor.close()
                    conexion.close()
                    return id_medico
                else:
                    print("ID de médico no válido.")
                    cursor.close()
                    conexion.close()
                    continue
        else:
            print("No hay médicos disponibles.")
            cursor.close()
            conexion.close()

    except mysql.connector.Error as error:
        print("Error al obtener la lista de médicos:", error)
        return None


def ingresar_disponibilidad_medico():
    """Esta función permite ingresar el horario de dispoibilidad del médico elegido en la 
    funcion (mostrar_medicos)
    INPUTS:
    -Fecha.
    -Hora."""
    
    id_medico = mostrar_medicos()
    if id_medico:
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="informatica1",
                password="bio123",
                database="informatica1"
            )
            cursor = conexion.cursor()

            continuar_ingresando = True
            print("[Fecha Disponible:]")
            while continuar_ingresando:
                #Estas funciones validan la fecha y hora (que estén dentro de rango temporal)
                while True:
                    ano=input("Ingrese el año: ")
                    try:
                        ano1=int(ano)
                        if len(ano)!=4:
                            print("El año debe tener 4 dígitos.")
                            continue
                        if validar_ano(ano1)==True:
                            break
                        elif validar_ano(ano1)==False:
                            print("Año invalido, ingrese año actual o futuro.")
                            continue    

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
                            print("Erro en  MES, ingrese mes actual o futuro.")
                            continue
                        if validar_mes(mes1,ano1)==True:
                            break
                        if validar_mes(mes1,ano1)==False:
                            continue
                        
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
                            print("Fecha invalida.")
                            continue
                        elif dia1>31 or dia1==0:
                            print("Error en DÍA, ingrese día válido.")
                            continue
                        elif mes1==4 or mes1==6 or mes1==9 or mes1==11  and dia1>30:
                            print("Error en DÍA, ingrese día válido.")
                            continue

                        if validar_dia(dia1,mes1)==True:
                            break
                        if validar_dia(dia1,mes1)==False:
                            continue
                        break
                    except ValueError:
                        print("Ingrese valores numericos.")
                        continue
                
                fecha = f"{ano}/{mes}/{dia}"
                print(fecha)
            
                print("[Hora Disponible:]")
                while True:
                    
                    hora = input("""Ingrese la hora disponible  (HH:MM): 
                    <Recuerde: El sistema usa formato de 24 horas>
                    >>""")
                    if len(hora)!=4 and len(hora)!=5:
                        print("Formato incorrecto de hora")
                        continue
                    if len(hora)==4:
                        if int(hora[:1])<7:
                            print("Horarios no disponibles la IPS abre a las 7:00 horas.")
                            continue
                        else:
                            break

                    if len(hora)==5: 
                        if 18<int(hora[:2]):
                            print("Horarios no disponibles la IPS cierra a las 18:00 horas.")
                            continue
                        else:
                            break

                    if validar_hora(hora,dia1)==True:
                        break
                    if validar_hora(hora,dia1)==False:
                        continue
                    else:
                        break

                fecha_hora = f"{fecha} {hora}"

                consulta_insertar = "INSERT INTO disponibilidad_medicos (id_medico, fecha_disponible,hora) VALUES (%s, %s,%s)"
                datos = (id_medico, fecha, hora)
                cursor.execute(consulta_insertar, datos)
                conexion.commit()

                continuar = input("¿Desea ingresar otra fecha y hora? (Si/No): ")
                if continuar.lower() != 'si' :
                    continuar_ingresando = False

                print("Disponibilidad del médico ingresada correctamente.")

            cursor.close()
            conexion.close()

        except mysql.connector.Error as error:
            print("Error al ingresar disponibilidad del médico:", error)

# ingresar_disponibilidad_medico()