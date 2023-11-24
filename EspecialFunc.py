usuario={"1054090489":"LAURA415","1036964559":"JUAND123","informatica1":"bio123"}

def logusuarios():
    """Esta función permite que los usuarios ya registrados accedan al sistema de géstión.
    INPUTS:
    -Identificación. (usada como usuario)
    -Contraseña.  """
    
    
    while True:
        # try:
        name=input("""Ingrese el ususario:
        (Número de Identificación o Usuario Asignado)
        >>> """)
            # break 
        # except ValueError:
        #     print("Ingresa un valor númerico.")
        if 7>len(name) or len(name)>12:
            print("La cantidad de dígitos del número de identificación no está dentro del rango de 7 a 11. ")
            continue

        password=input("Ingrese su contraseña: ")
        if name in usuario and usuario[name]==password:
            break
        else: 
            print("""Usuario u contraseña equivocada.
                Intente nuevamente.""")
            continue

            
def newuser():
    """Esta función permite que los usuarios ya registrados puedan crear un nuevo usuario
    INPUTS:
    -Identificación. (usada como usuario)
    -Contraseña. """
    
    newuser=input("Ingrese el número de identificación del nuevo usuario: ")
    newpass=input("Ingrese la clave del nuevo usuario: ")
    usuario.update({newuser:newpass})

def validar_ano(ano1):
    """Esta función permite validar que el año ingresado para programar
      la disponibilidad, sea actual o futuro y no un año pasado.
      INPUTS:
      -Año"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    ano2=str(hora)
    ver_ano=int(ano2[:4])
    
    if ano1<ver_ano:
        return False
    else:
        return True
    
def validar_mes(mes1,ano1):
    """Esta función permite validar que el mes ingresado para programar
      la disponibilidad, sea actual o futuro y no un mes pasado.
      INPUTS:
      -Mes"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    mes2=str(hora)
    ver_mes=int(mes2[5:7])
    if ano1==int(mes2[:4]):
        if mes1<ver_mes:
            print("Mes invalido, ingrese mes actual o futuro.")
            return False
        else:
            return True

def validar_dia(dia1,mes1):
    """Esta función permite validar que el día ingresado para programar
      la disponibilidad, sea actual o futuro y no un día pasado.
      INPUTS:
      -Día"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    dia2=str(hora)
    ver_día=int(dia2[8:11])
    if mes1==int(dia2[5:7]):
        if dia1<ver_día:
            print("Día invalido, ingrese día actual o futuro.")
            return False
        else:
            return True

def validar_hora(hora,dia1):
    """Esta función permite validar que la hora ingresado para programar
      la disponibilidad, sea actual o futuro y no una hora pasada.
      INPUTS:
      -Hora"""
    if len(hora)==4:
        hora1=int(hora[:1])
        min1=int(hora[2:4])
    elif len(hora)==5:
        hora1=int(hora[:2])
        min1=int(hora[3:5])
    import datetime
    hora=datetime.datetime.now()
    hora2=str(hora)
   
    ver_hora=int(hora2[11:13])
    ver_min=int(hora2[14:16])
    if dia1==int(hora2[8:11]):
        if hora1<ver_hora:
            print("Hora invalida, ingrese hora actual o futura.")
            return False
        if min1<ver_min:
            print(" Hora invalida, ingrese hora actual o futura.")
            return False
        else:
            return True

def validar_anonac(ano1):
    """Esta función permite validar que el año ingresado de la fecha de
    nacimiento, sea actual o pasado y no un año futuro.
      INPUTS:
      -Año"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    ano2=str(hora)
    ver_ano=int(ano2[:4])
    
    if ano1>ver_ano:
        return False
    else:
        return True
    
def validar_mesnac(mes1,ano1):
    """Esta función permite validar que el mes ingresado de la fecha de
    nacimiento, sea actual o pasado y no un mes futuro.
      INPUTS:
      -Mes"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    mes2=str(hora)
    ver_mes=int(mes2[5:7])
    if ano1==int(mes2[:4]):
        if mes1>ver_mes:
            return False
        else:
            return True

def validar_dianac(dia1,mes1,ano1):
    """Esta función permite validar que el día ingresado de la fecha de
    nacimiento, sea actual o pasado y no un día futuro.
      INPUTS:
      -Día"""
    import datetime
    hora=datetime.datetime.now()
    # print(hora)
    dia2=str(hora)
    ver_día=int(dia2[8:11])
    if mes1==int(dia2[5:7])and ano1==int(dia2[:4]):
        if dia1>ver_día:
            return False
        else:
            return True