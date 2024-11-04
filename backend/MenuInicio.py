#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# VARIABLES
#----------------------------------------------------------------------------------------------
DiccionarioUsuarios={}
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(personas):
    """
    Añade un nuevo cliente al diccionario de usuarios.

    Parametros:
    personas (diccionario): Diccionario que contiene los datos de los clientes.

    Retorna:
    None
    """
    while True:
        idNueva = int(input("Ingrese un ID para el nuevo cliente: "))
        if idNueva not in personas:
            break
        else:
            print("El ID ya existe, por favor ingrese otro ID")
         
    nombre = input("Ingrese el nombre y apellido: ")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso (kg): "))
    altura = int(input("Ingrese la altura (cm): "))
    
    while True:
        print("Seleccione el sexo:")
        print("[1] Masculino (M)")
        print("[2] Femenino (F)")
        opcion_sexo = input("Ingrese el número correspondiente a su opción: ")
        
        if opcion_sexo == "1":
            sexo = "M"
            break
        elif opcion_sexo == "2":
            sexo = "F"
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    while True:
        print("Seleccione el estado del cliente:")
        print("[1] Activo")
        print("[2] Inactivo")
        opcion_estado = input("Ingrese el número correspondiente a su opción: ")
        
        if opcion_estado == "1":
            estado = "activo"
            break
        elif opcion_estado == "2":
            estado = "inactivo"
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    while True:
        print("Seleccione el estado de la membresía:")
        print("[1] Paga")
        print("[2] Pendiente")
        print("[3] Inpaga")
        opcion_membresia = input("Ingrese el número correspondiente a su opción: ")
        
        if opcion_membresia == "1":
            membresia = "paga"
            break
        elif opcion_membresia == "2":
            membresia = "pendiente"
            break
        elif opcion_membresia == "3":
            membresia = "inpaga"
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    while True:
        print("Seleccione el objetivo:")
        print("[1] Aumentar masa muscular")
        print("[2] Disminuir grasa corporal")
        print("[3] Mantener estado físico")
        opcion_objetivo = input("Ingrese el número correspondiente a su opción: ")
        
        if opcion_objetivo == "1":
            objetivo = "aumentar masa muscular"
            break
        elif opcion_objetivo == "2":
            objetivo = "disminuir grasa corporal"   
            break
        elif opcion_objetivo == "3":
            objetivo = "mantener estado físico"
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    print(f"Persona con ID {idNueva} agregada exitosamente.")
    
    personas[idNueva] = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "altura": altura,
        "sexo": sexo,
        "objetivo": objetivo,
        "estado": estado,
        "membresia": membresia,
    }
    print()
    print("---------------------------")
    print("CLIENTES ACTUALIZADOS")
    print("---------------------------")
    print("{:^5} | {:^20} | {:^5} | {:^5} | {:^7} | {:^5} | {:^30} | {:^10} | {:^10} |".format(
        "ID", "Nombre", "Edad", "Peso", "Altura", "Sexo", "Objetivo", "Membresia", "Estado"
    ))
    print("-" * 125)
    for id, cliente in personas.items():
        print("{:^5} | {:^20} | {:^5} | {:^5} | {:^7} | {:^5} | {:^30} | {:^10} | {:^10} |".format(
            id, cliente["nombre"], cliente["edad"], cliente["peso"], cliente["altura"], cliente["sexo"], cliente["objetivo"], cliente["membresia"], cliente["estado"]
        ))
    print("-" * 125)

def modificarCliente(personas):
    """
    Modifica los atributos de un cliente en el diccionario de usuarios.

    Parametros:
    personas (diccionario): Diccionario que contiene los datos de los clientes.

    Retorna:
    None
    """
    while True:
        id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
        if id_cliente in personas:
            print("--------------------")
            print("CLIENTE ENCONTRADO")
            print("--------------------")
            print()
                        
            print("{:<10} | {:<20} | {:<5} | {:<5} | {:<7} | {:<5} | {:<30} | {:<10} | {:<10} |".format(
                "ID", "Nombre", "Edad", "Peso", "Altura", "Sexo", "Objetivo", "Membresia", "Estado"
            ))
            print("-" * 125)
            print("{:<10} | {:<20} | {:<5} | {:<5} | {:<7} | {:<5} | {:<30} | {:<10} | {:<10} |".format(
                id_cliente, personas[id_cliente]["nombre"], personas[id_cliente]["edad"], 
                personas[id_cliente]["peso"], personas[id_cliente]["altura"], 
                personas[id_cliente]["sexo"], personas[id_cliente]["objetivo"], 
                personas[id_cliente]["membresia"], personas[id_cliente]["estado"]
            ))
            print()
            print("¿QUÉ DESEA MODIFICAR?")
            print("[1] Nombre")
            print("[2] Edad")
            print("[3] Peso")
            print("[4] Altura")
            print("[5] Sexo")
            print("[6] Objetivo")
            print("[7] Membresía")
            print("[8] Estado")
            print("[9] Salir")
            
            atributo = int(input("Ingrese el atributo que desea modificar: "))
            if atributo == 1:
                personas[id_cliente]["nombre"] = input("Ingrese el nuevo nombre: ")
            elif atributo == 2:
                personas[id_cliente]["edad"] = int(input("Ingrese la nueva edad: "))
            elif atributo == 3:
                personas[id_cliente]["peso"] = float(input("Ingrese el nuevo peso: "))
            elif atributo == 4:
                personas[id_cliente]["altura"] = int(input("Ingrese la nueva altura: "))
            elif atributo == 5:
                while True:
                    sexo = input("Ingrese el nuevo sexo (M/F): ").upper()
                    if sexo in ["M", "F"]:
                        personas[id_cliente]["sexo"] = sexo
                        break
                    else:
                        print("Sexo no válido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")
            elif atributo == 6:
                personas[id_cliente]["objetivo"] = input("Ingrese el nuevo objetivo: ")
            elif atributo == 7:
                personas[id_cliente]["membresia"] = input("Ingrese la nueva membresía: ")
            elif atributo == 8:
                while True:
                    estado = input("Ingrese el nuevo estado (Activo/Inactivo): ").lower()
                    if estado in ["activo", "inactivo"]:
                        personas[id_cliente]["estado"] = estado
                        break
                    else:
                        print("Estado no válido. Por favor, ingrese 'Activo' o 'Inactivo'.")
            elif atributo == 9:
                print("SALIENDO...")
                break
            else:
                print("Opción no válida.")
                
            print("\n{:<10} | {:<20} | {:<5} | {:<5} | {:<7} | {:<5} | {:<30} | {:<10} | {:<10} |".format(
                "ID", "Nombre", "Edad", "Peso", "Altura", "Sexo", "Objetivo", "Membresia", "Estado"
            ))
            print("-" * 125)
            print("{:<10} | {:<20} | {:<5} | {:<5} | {:<7} | {:<5} | {:<30} | {:<10} | {:<10} |".format(
                id_cliente, personas[id_cliente]["nombre"], personas[id_cliente]["edad"], 
                personas[id_cliente]["peso"], personas[id_cliente]["altura"], 
                personas[id_cliente]["sexo"], personas[id_cliente]["objetivo"], 
                personas[id_cliente]["membresia"], personas[id_cliente]["estado"]
            ))
        else:
            print("Usuario no encontrado.")

def inactivarClientes(personas):
    """
    Inactiva un cliente cambiando su estado a 'inactivo'.

    Parametros:
    personas (dict): Diccionario que contiene los datos de los clientes.

    Retorna:
    diccionario: Diccionario actualizado con el cliente inactivado.
    """
    print("\nInactivar Cliente")
    print("------------------")
    id_cliente = int(input("Ingrese el ID del cliente a inactivar: "))
    if id_cliente in personas:
        if personas[id_cliente]["estado"]=="activo":
            personas[id_cliente]["estado"] = "inactivo"
            print(f"Cliente {personas[id_cliente]['nombre']} inactivado con éxito.")
        else:
            print(f"El cliente {personas[id_cliente]['nombre']} ya estaba inactivo.")
    else:
        print("Cliente no encontrado")
    return personas

def listadoClientes(personas):
    """
    Muestra el listado de clientes registrados en formato tabular.

    Parametros:
    personas (diccionario): Diccionario que contiene los datos de los clientes.

    Retorna:
    None
    """
    print()
    print("---------------------------")
    print("USUARIOS REGISTRADOS       ")
    print("---------------------------")
    print("{:^5} | {:^20} | {:^5} | {:^5} | {:^7} | {:^5} | {:^30} | {:^10} | {:^10} |".format(
        "ID", "Nombre", "Edad", "Peso", "Altura", "Sexo", "Objetivo", "Membresia", "Estado"
    ))
    print("-" * 125)
    for id, cliente in personas.items():
        print("{:^5} | {:^20} | {:^5} | {:^5} | {:^7} | {:^5} | {:^30} | {:^10} | {:^10} |".format(
            id, cliente["nombre"], cliente["edad"], cliente["peso"], cliente["altura"], cliente["sexo"], cliente["objetivo"], cliente["membresia"], cliente["estado"]
        ))
    print("-" * 125)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal que controla el flujo del programa a través de un menú.

    Retorna:
    None
    """
    personas = {
    1: {"estado":  "activo","membresia": "Paga","nombre": "Juan Pérez", "edad": 25, "peso": 70, "altura": 175, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    2: {"estado":  "activo","membresia": "Paga","nombre": "Ana López", "edad": 30, "peso": 65, "altura": 160, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    3: {"estado":  "activo","membresia": "Paga","nombre": "Carlos García", "edad": 35, "peso": 80, "altura": 180, "sexo": "M", "objetivo": "Mantener estado físico"},
    4: {"estado":  "activo","membresia": "Paga","nombre": "María Rodríguez", "edad": 28, "peso": 55, "altura": 165, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    5: {"estado":  "activo","membresia": "Paga","nombre": "Pedro Sánchez", "edad": 40, "peso": 90, "altura": 185, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    6: {"estado":  "activo","membresia": "Paga","nombre": "Lucía Fernández", "edad": 22, "peso": 50, "altura": 158, "sexo": "F", "objetivo": "Mantener estado físico"},
    7: {"estado":  "activo","membresia": "Paga","nombre": "Javier Morales", "edad": 27, "peso": 85, "altura": 178, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    8: {"estado":  "activo","membresia": "Paga","nombre": "Laura Díaz", "edad": 33, "peso": 68, "altura": 162, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    9: {"estado":  "activo","membresia": "Paga","nombre": "Fernando Torres", "edad": 29, "peso": 77, "altura": 177, "sexo": "M", "objetivo": "Mantener estado físico"},
    10: {"estado": "activo","membresia": "Paga","nombre": "Isabel Gómez", "edad": 36, "peso": 60, "altura": 170, "sexo": "F", "objetivo": "Aumentar masa muscular"},
    11: {"estado": "activo","membresia": "Paga","nombre": "Alberto Ruiz", "edad": 31, "peso": 95, "altura": 190, "sexo": "M", "objetivo": "Disminuir grasa corporal"},
    12: {"estado": "activo","membresia": "Paga","nombre": "Carmen Vargas", "edad": 26, "peso": 58, "altura": 160, "sexo": "F", "objetivo": "Mantener estado físico"},
    13: {"estado": "activo","membresia": "Paga","nombre": "Roberto Castro", "edad": 34, "peso": 85, "altura": 175, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    14: {"estado": "activo","membresia": "Paga","nombre": "Elena Ramírez", "edad": 24, "peso": 52, "altura": 163, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    15: {"estado": "activo","membresia": "Paga","nombre": "Diego Herrera", "edad": 37, "peso": 82, "altura": 180, "sexo": "M", "objetivo": "Mantener estado físico"},
    16: {"estado": "activo","membresia": "Paga","nombre": "Patricia Ortiz", "edad": 32, "peso": 66, "altura": 167, "sexo": "F", "objetivo": "Aumentar masa muscular"},
    17: {"estado": "activo","membresia": "Paga","nombre": "Raúl Reyes", "edad": 29, "peso": 90, "altura": 182, "sexo": "M", "objetivo": "Disminuir grasa corporal"},
    18: {"estado": "activo","membresia": "Paga","nombre": "Beatriz Romero", "edad": 25, "peso": 54, "altura": 160, "sexo": "F", "objetivo": "Mantener estado físico"},
    19: {"estado": "activo","membresia": "Paga","nombre": "Hugo Delgado", "edad": 28, "peso": 88, "altura": 178, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    20: {"estado": "activo","membresia": "Paga","nombre": "Marta Jiménez", "edad": 30, "peso": 61, "altura": 165, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    21: {"estado": "activo","membresia": "Paga","nombre": "Luis Navarro", "edad": 26, "peso": 72, "altura": 174, "sexo": "M", "objetivo": "Mantener estado físico"},
    22: {"estado": "activo","membresia": "Paga","nombre": "Alicia Santos", "edad": 35, "peso": 63, "altura": 168, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    23: {"estado": "activo","membresia": "Paga","nombre": "Francisco Méndez", "edad": 33, "peso": 78, "altura": 176, "sexo": "M", "objetivo": "Mantener estado físico"},
    24: {"estado": "activo","membresia": "Paga","nombre": "Julia Pérez", "edad": 31, "peso": 59, "altura": 160, "sexo": "F", "objetivo": "Aumentar masa muscular"},
    25: {"estado": "activo","membresia": "Paga","nombre": "Antonio Silva", "edad": 38, "peso": 92, "altura": 183, "sexo": "M", "objetivo": "Disminuir grasa corporal"},
    26: {"estado": "activo","membresia": "Paga","nombre": "Sara Martín", "edad": 23, "peso": 57, "altura": 162, "sexo": "F", "objetivo": "Mantener estado físico"},
    27: {"estado": "inactivo","membresia":"Inpaga","nombre": "Manuel Espinosa", "edad": 29, "peso": 86, "altura": 179, "sexo": "M", "objetivo": "Aumentar masa muscular"},
    28: {"estado": "inactivo","membresia":"Inpaga","nombre": "Cristina Gil", "edad": 30, "peso": 62, "altura": 166, "sexo": "F", "objetivo": "Disminuir grasa corporal"},
    29: {"estado": "inactivo","membresia":"Inpaga","nombre": "Gabriel Alonso", "edad": 27, "peso": 84, "altura": 180, "sexo": "M", "objetivo": "Mantener estado físico"},
    30: {"estado": "inactivo","membresia":"Pendiente","nombre": "Verónica Iglesias", "edad": 34, "peso": 60, "altura": 164, "sexo": "F", "objetivo": "Aumentar masa muscular"}}
    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 5
        while True: 
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Gestión de Clientes")
            print("[2] Gestión de Rutinas")
            print("[3] Gestión de Dietas")
            print("[4] Informes Generales")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":
            OpcionesMenuGestionClientes=5
            while True:
                print()
                print("---------------------------")
                print("MENU GESTIÓN DE CLIENTES")
                print("---------------------------")
                print("[1] Ingresar Cliente")
                print("[2] Modificar Cliente")
                print("[3] Inactivar Cliente")
                print("[4] Emitir listado Clientes")
                print("[0] Volver al menú")
                OpcionMenuGestionClientes=input("Seleccione una opción: ")
                if OpcionMenuGestionClientes in [str(i) for i in range(0, OpcionesMenuGestionClientes)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()
            if OpcionMenuGestionClientes=="1":
                altaCliente(personas)
            elif OpcionMenuGestionClientes=="2":
                modificarCliente(personas)
            
            elif OpcionMenuGestionClientes=="3":
               inactivarClientes(personas)
        
            
            elif OpcionMenuGestionClientes=="4":
                listadoClientes(personas)
            
            elif OpcionMenuGestionClientes=="0":
                exit()
            
            
        elif opcion == "2":
                OpcionesMenuGestionRutinas=4
                print()
                print("---------------------------")
                print("MENU GESTIÓN DE RUTINAS")
                print("---------------------------")
                print("[1] Asignar nueva rutina")
                print("[2] Modificar Rutina")
                print("[3] Emitir Resumen de Rutinas asignadas")
                print("[0] Volver al menú")
                OpcionMenuGestionRutinas=input("Seleccione una opción: ")
                if OpcionMenuGestionRutinas in [str(i) for i in range(0, OpcionesMenuGestionRutinas)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                if OpcionMenuGestionRutinas=="1":
                    ...
                elif OpcionMenuGestionRutinas=="2":
                    ...
                elif OpcionMenuGestionRutinas=="3":
                    ...
                elif OpcionMenuGestionRutinas=="0":
                    return
        elif opcion == "3":
            OpcionesMenuGestionDietas=4
            print()
            print("---------------------------")
            print("MENU GESTIÓN DE DIETAS")
            print("---------------------------")
            print("[1] Asignar nueva Dieta")
            print("[2] Modificar Dieta")
            print("[3] Emitir Resumen de Dietas asignadas")
            print("[0] Volver al menú")
            OpcionMenuGestionDietas=input("Seleccione una opción: ")
            if OpcionMenuGestionDietas in [str(i) for i in range(0, OpcionesMenuGestionDietas)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()
            if OpcionMenuGestionDietas=="1":
                ...
            elif OpcionMenuGestionDietas=="2":
                ...
            elif OpcionMenuGestionDietas=="3":
                ...
            elif OpcionMenuGestionDietas=="0":
                return
            
        elif opcion == "4":
            OpcionesInformesGenerales=5
            print()
            print("---------------------------")
            print("INFORMES GENERALES")
            print("---------------------------")
            print("[1] Emitir Informe de membresía de los clientes")
            print("[2] Emitir Informe de Rutinas y Dietas de los clientes")
            print("[3] Emitir Informe de Clientes Inactivos")
            print("[0] Volver al menú")
            OpcionInformesGenerales=input("Seleccione una opción: ")
            if OpcionInformesGenerales in [str(i) for i in range(0, OpcionesInformesGenerales)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()
            if OpcionInformesGenerales=="1":
                ...
            elif OpcionInformesGenerales=="2":
                ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()