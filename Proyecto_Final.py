#Laura Jimena Munevar Mora <1054090489>
#Juan Diego Hernandez <1036964559>
from EspecialFunc import*
from Create import*
from Update_act import*
from Search import*
from Read_comp_inf import*
from Delete import*
from Validation_p_m import*
from Citas import*
from Disponibility import*
from Search_cita import*
print("""                   SISTEMA DE GESTIÓN DE CITAS MEDICAS
                                    Hospital Universitario:
            ___________________________________________________________________________
      
                                        Bienvenido.
      
A continuación, encotrará el menú principal.
      """)

while True:
    while True:
        try:
            menu1=int(input("""Ingrese el número correspondiente a la operación que desea realzar:
                            
                            1.<PACIENTE> Consulta, modificación y cancelación de citas medicas.
                            2.<MÉDICO> Consulta de pacientes, citas asignadas y disponibilidad de agenda.
                            3.<ADMINISTRADOR> Gestión de información hospitalaria.
                            4.Salir del sistema.
                            > """))
            if menu1 >4:
                print("Ingrese un valor válido.")
                continue
            elif menu1==0:
                print("Ingrese un valor válido.")
                continue   
            break
        except ValueError:
            print("Ingrese valores numericos.")
            continue


    if menu1==1:
        print("             >>>CONSULTA, MODIFICACIÓN Y CANCELACIÓN DE CITAS MÉDICAS.<<<")
        if validar_paciente()==True:
            while True:
                try:
                    menua=int(input("""Ingrese el número correspondiente a la operación que desea realizar.
                                1.Consultar cita medica.
                                2.Modificar una cita médica.
                                3.Cancelar una cita médica.
                                4.Volver al menú principal.
                                > """))
                    if menua >4:
                        print("Ingrese un valor válido.")
                        continue
                    elif menua==0:
                        print("Ingrese un valor válido.")
                        continue
                    
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue

                if menua==1:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menua==2:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menua==3:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menua==4:
                    print("              <<<Volviendo al menú.>>>")
                    break
                

    elif menu1==2:
        print("             >>>CONSULTA DE PACIENTES,CITAS ASIGNADAS Y DISPONIBILIDAD DE AGENDA.<<<")
        if validar_medico()==True:
            while True:
                try:
                    menub=int(input("""Ingrese el número correspondiente a la operación que desea realizar.
                                1.Ver agenda de citas diarias.
                                2.Ver agenda de citas semanales.
                                3.Ver e indicar disponibilidad de angenda.
                                4.Cancelación de cita.
                                5.Volver al menú principal.
                                > """))
                    if menub >5: 
                        print("Ingrese un valor válido.")
                        continue
                    elif menub==0:
                        print("Ingrese un valor válido.")
                        continue
                    
                except ValueError:
                    print("Ingrese valores numericos.")
                    continue
                

                if menub==1:
                    print("Función NO DISPONIBLE.")
                    continue
                    
                elif menub==2:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menub==3:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menub==4:
                    print("Función NO DISPONIBLE.")
                    continue

                elif menub==5:
                    print("              <<<Volviendo al menú.>>>")
                    break

    elif menu1==3:
        print("             >>>GESTIÓN DE INFORMACIÓN HOSPITALARIA.<<<")
        logusuarios()
        #FUNCION para verificar que el ususario y la contraseña esten registrados.
        while True:
            try:
                menu2=int(input("""Ingrese el número correspondiente a la operación que desea realzar:
                                
                                1.Gestión de Pacientes.
                                2.Gestión de Medicos.
                                3.Gestión de citas medicas.
                                4.Agregar usuario.
                                5.Volver al menú principal.
                                >"""))
                if menu2 >5:
                    print("Ingrese un valor válido.")
                    continue
                elif menu2==0:
                    print("Ingrese un valor válido.")
                    continue  

            except ValueError:
                print("Ingrese valores numericos.")
                continue
            
            if menu2==1:
                while True:
                    try:
                        menupac=int(input("""Ingrese el número correspondiente a la operación que desea realzar:
                                        
                                        1.Ingresar un nuevo paciente.
                                        2.Actualizar información de un paciente.
                                        3.Buscar un paciente.
                                        4.Ver información de todos los pacientes.
                                        5.Eliminar un paciente.
                                        6.Volver al menú principal.
                                        >"""))
                        if menupac >6:
                            print("Ingrese un valor válido.")
                            continue
                        elif menupac==0:
                            print("Ingrese un valor válido.")
                            continue
                    
                    except ValueError:
                        print("Ingrese valores numericos.")
                        continue
                    if menupac==1:
                        ingresar_paciente()
                        continue
                    if menupac==2:
                        print("             >>>Actualización de información.<<<")
                        actualizar_paciente()
                        continue 
                    elif menupac==3:
                        
                        print("             >>>Buscar paciente.<<<")
                        buscar_paciente()
                        continue
                    elif menupac==4:
                        leer_infopac()
                        continue
                    elif menupac==5:
                        
                        print("             >>>Eliminar un paciente.<<<")
                        eliminar_pacientes()
                        continue
                    elif menupac==6:
                        print("             <<<Volviendo al menú.>>>")
                        break
                                            
            elif menu2==2:
                while True:
                    try:
                        menumed=int(input("""Ingrese el número correspondiente a la operación que desea realzar:
                                        
                                        1.Ingresar un nuevo médicos.
                                        2.Actualizar información de un médicos.
                                        3.Buscar un médicos.
                                        4.Ver información de todos los médicos.
                                        5.Eliminar un médicos.
                                        6.Ingresar la disponibilidad del médico.
                                        7.Volver al menú principal.
                                        >"""))
                        if menumed >7:
                            print("Ingrese un valor válido.")
                            continue
                        elif menumed==0:
                            print("Ingrese un valor válido.")
                            continue

                    except ValueError:
                        print("Ingrese valores numericos.")
                        continue

                    if menumed==1:
                        ingresar_medico()
                        continue
                    elif menumed==2:
                        print("             >>>Actualización de información.<<<")
                        actualizar_medico()
                        continue

                    elif menumed==3:
                        print("             >>>Busqueda de un médico.<<<")
                        buscar_medico()
                        continue
                    elif menumed==4:
                        leer_infomed()
                        continue
                    elif menumed==5:
                        print("             >>>Eliminar un médico.<<<")
                        eliminar_medico_con_citas()
                        continue
                    elif menumed==6:
                        print("             >>>Disponibilidad.<<<")
                        ingresar_disponibilidad_medico()
                        continue
                    elif menumed==7:
                        print("             <<<Volviendo al menú.>>>")
                        break


            elif menu2==3:
                while True:
                    try:
                        menucitas=int(input("""Ingrese el número correspondiente a la operación que desea realzar:
                                        
                                        1.Programar cita médica.
                                        2.Consultar cita médica.
                                        3.Actualizar cita médica.
                                        4.Cancelar cita médica.
                                        5.Recordatorio de cita médica.
                                        6.Volver al menú principal.
                                        >"""))
                        if menucitas>6:
                            print("Ingrese un valor válido.")
                            continue
                        elif menucitas==0:
                            print("Ingrese un valor válido.")
                            continue
                    
                    except ValueError:
                        print("Ingrese valores numericos.")
                        continue

                    if menucitas==1:
                        programar_cita()
                        continue

                    elif menucitas==2:
                        revisar_citas_paciente()
                        continue

                    elif menucitas==3:
                        print("Función NO DISPONIBLE.")
                        continue

                    elif menucitas==4:
                        print("Función NO DISPONIBLE.")
                        continue

                    elif menucitas==5:
                        print("Función NO DISPONIBLE.")
                        continue

                    elif menucitas==6:
                        break
                
            elif menu2==4:
                #Funcion para agregar nuevos usuarios, si embargo no se si meterla en una base de datos.
                newuser()
                print(usuario)   
            elif menu2==5:
                print("              <<<Volviendo al menú.>>>")
                break

                
    elif menu1==4:
        print("              <<<Saliendo del Sistema.>>>")
        break







