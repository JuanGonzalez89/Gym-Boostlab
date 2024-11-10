#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
import json
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
    
# Función para cargar datos desde un archivo JSON
def cargarDatos(archivoJson):
    try:
        with open(archivoJson, 'r') as archivo:  # Abre el archivo en modo lectura
            return json.load(archivo)  # Carga el contenido del archivo JSON y lo convierte a un diccionario de Python
    except FileNotFoundError:
        return {}  # Si el archivo no existe, retorna un diccionario vacío
    except json.JSONDecodeError:
        print("Error, archivo JSON no valido")  # Maneja el error si el archivo no es un JSON válido
        return {}
    
# Función para guardar datos en un archivo JSON
def guardarDatos(archivoJson, datos):
    with open(archivoJson, 'w') as archivo:  # Abre el archivo en modo escritura
        json.dump(datos, archivo, indent=4)  # Convierte el diccionario de Python a formato JSON y lo guarda en el archivo

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal que controla el flujo del programa a través de un menú.

    Retorna:
    None
    """
    personas = cargarDatos('clientes.json')  # Carga los datos de clientes desde el archivo JSON
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
    
    rutinas = {
    #----------------------------------------------------------------------------------------------
    #RUTINAS DISMINUIR GRASA CORPORAL
    #----------------------------------------------------------------------------------------------
    1: {
        "Nombre": "Circuito HIIT para Quema de Grasa",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 15-20 reps",
        "Ejercicios": ["Burpees", "Mountain climbers", "Sprints en cinta", "Box jumps", "Salto a la cuerda"]
    },
    2: {
        "Nombre": "Cardio Funcional de Alta Intensidad",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 12-15 reps",
        "Ejercicios": ["Swing con kettlebell", "Jumping jacks", "Remo", "Sentadilla con salto", "Escaladora"]
    },
    3: {
        "Nombre": "Definición Dinámica de Tren Inferior",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "3 series de 15 reps",
        "Ejercicios": ["Sentadillas con peso corporal", "Desplantes con salto", "Sentadilla con salto", "Mountain climbers", "Flexiones explosivas"]
    },
    4: {
        "Nombre": "Circuito de Core Intenso",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 20 reps",
        "Ejercicios": ["Plancha", "Crunch bicicleta", "Russian twists", "Mountain climbers", "Elevaciones de piernas"]
    },
    5: {
        "Nombre": "Quema Grasa con Peso Corporal",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 12-20 reps",
        "Ejercicios": ["Burpees", "Plank", "Sentadilla con salto", "Jumping jacks", "Lunges"]
    },
    6: {
        "Nombre": "Entrenamiento de Cardio Potente",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 15 reps",
        "Ejercicios": ["Sprints en cinta", "Remo", "Mountain climbers", "Burpees", "Flexiones"]
    },
    7: {
        "Nombre": "Definición Corporal Total",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Media",
        "Repeticiones": "3 series de 15 reps",
        "Ejercicios": ["Box jumps", "Jump rope", "Sentadilla de peso corporal", "Escaladora", "Russian twists"]
    },
    8: {
        "Nombre": "Ejercicios de Resistencia y Definición",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 12-15 reps",
        "Ejercicios": ["Battleropes", "Swing con kettlebell", "Remo", "Plank", "Box jumps"]
    },
    9: {
        "Nombre": "Rutina de Cardio y Core",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 15 reps",
        "Ejercicios": ["Mountain climbers", "Plancha con toque de hombros", "Russian twists", "Salto a la cuerda", "Escaladora"]
    },
    10: {

        "Nombre": "Quema Rápida de Calorías",
        "Dias": 5,
        "Tipo": "Disminuir grasa corporal",
        "Intensidad": "Alta",
        "Repeticiones": "5 series de 15 reps",
        "Ejercicios": ["Sprint en cinta", "Sentadillas con salto", "Burpees", "Escaladora", "Plank"]
    },
    #----------------------------------------------------------------------------------------------
    #RUTINAS MANTENER ESTADO FISICO
    #----------------------------------------------------------------------------------------------
    11: {

        "Nombre": "Rutina de Mantenimiento Corporal Completo",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "3 series de 10-12 reps",
        "Ejercicios": ["Sentadilla con peso corporal", "Flexiones", "Remo con banda", "Desplantes", "Plancha"]
    },
    12: {

        "Nombre": "Circuito de Resistencia Funcional",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 12 reps",
        "Ejercicios": ["Estocadas", "Press militar", "Sentadilla con peso corporal", "Plank", "Remo sentado"]
    },
    13: {

        "Nombre": "Tonificación con Peso Corporal",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "3 series de 10 reps",
        "Ejercicios": ["Sentadilla", "Plancha lateral", "Push ups", "Estocadas laterales", "Elevación de talones"]
    },
    14: {

        "Nombre": "Entrenamiento Corporal Básico",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Baja",
        "Repeticiones": "3 series de 12 reps",
        "Ejercicios": ["Sentadilla de peso corporal", "Lunges", "Flexiones", "Remo con banda", "Elevación de piernas"]
    },
    15: {

        "Nombre": "Core y Resistencia General",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 10-12 reps",
        "Ejercicios": ["Plancha", "Crunchs", "Lunges", "Mountain climbers", "Press militar"]
    },
    16: {

        "Nombre": "Circuito de Fuerza Moderada",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 12 reps",
        "Ejercicios": ["Flexiones", "Sentadillas", "Remo con bandas", "Press militar", "Estocadas"]
    },
    17: {

        "Nombre": "Resistencia para Todo el Cuerpo",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 10 reps",
        "Ejercicios": ["Press militar", "Desplantes", "Push-ups", "Crunch", "Elevaciones de talones"]
    },
    18: {

        "Nombre": "Fortalecimiento y Flexibilidad",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 10 reps",
        "Ejercicios": ["Estocadas", "Plancha", "Bird dog", "Lunge", "Push ups"]
    },
    19: {

        "Nombre": "Ejercicios de Equilibrio y Mantenimiento",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "3 series de 12 reps",
        "Ejercicios": ["Remo con bandas", "Sentadilla", "Desplantes", "Push ups", "Plank"]
    },
    20: {

        "Nombre": "Resistencia Corporal Completa",
        "Dias": 5,
        "Tipo": "Mantener estado físico",
        "Intensidad": "Media",
        "Repeticiones": "4 series de 12 reps",
        "Ejercicios": ["Sentadilla", "Flexiones", "Crunch abdominal", "Plancha", "Remo con banda"]
    },
    #----------------------------------------------------------------------------------------------
    #MANTENER ESTADO FISICO
    #----------------------------------------------------------------------------------------------
    21: {

        "Nombre": "Hipertrofia en Pecho y Espalda",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8-10 reps",
        "Ejercicios": ["Press de banca", "Remo con barra", "Press inclinado", "Pullover", "Pull ups"]
    },
    22: {

        "Nombre": "Desarrollo de Brazos y Hombros",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8-10 reps",
        "Ejercicios": ["Curl de bíceps", "Press militar", "Press con mancuernas", "Extensión de tríceps", "Elevaciones laterales"]
    },
    23: {

        "Nombre": "Hipertrofia en Tren Inferior",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 10 reps",
        "Ejercicios": ["Sentadillas", "Peso muerto", "Prensa", "Curl de pierna", "Extensiones de pierna"]
    },
    24: {

        "Nombre": "Rutina de Potencia de Espalda y Bíceps",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8-10 reps",
        "Ejercicios": ["Dominadas", "Remo con barra", "Curl de bíceps con barra", "Pullover", "Remo con mancuernas"]
    },
    25: {

        "Nombre": "Hipertrofia de Piernas y Glúteos",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 10 reps",
        "Ejercicios": ["Sentadilla profunda", "Peso muerto rumano", "Prensa de piernas", "Hip thrust", "Zancadas con mancuernas"]
    },
    26: {

        "Nombre": "Fuerza y Volumen en Pecho y Tríceps",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8 reps",
        "Ejercicios": ["Press banca", "Press inclinado con mancuernas", "Fondos", "Extensión de tríceps", "Aperturas con mancuernas"]
    },
    27: {

        "Nombre": "Crecimiento Corporal Completo",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8-10 reps",
        "Ejercicios": ["Sentadilla", "Press de banca", "Peso muerto", "Remo con barra", "Press militar"]
    },
    28: {

        "Nombre": "Volumen en Pecho, Espalda y Hombros",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8 reps",
        "Ejercicios": ["Press banca con barra", "Dominadas asistidas", "Remo con barra", "Press militar", "Elevaciones laterales"]
    },
    29: {

        "Nombre": "Hipertrofia de Tren Inferior",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8-12 reps",
        "Ejercicios": ["Prensa de piernas", "Extensión de cuádriceps", "Peso muerto rumano", "Sentadilla búlgara", "Elevación de talones"]
    },
    30: {

        "Nombre": "Masa Corporal Completa",
        "Dias": 5,
        "Tipo": "Aumentar masa muscular",
        "Intensidad": "Alta",
        "Repeticiones": "4 series de 8 reps",
        "Ejercicios": ["Press banca con barra", "Sentadilla profunda", "Peso muerto", "Press militar", "Curl de bíceps"]
    }
    }
    dietas = {
    #----------------------------------------------------------------------------------------------
    #DIETAS DEFICIT CALORICO
    #----------------------------------------------------------------------------------------------
    1: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Ensalada de pollo con espinacas y aguacate", "Sopa de verduras con pechuga de pollo", "Salmón al horno con espárragos", "Tortilla de claras con espinacas", "Arroz integral con brócoli y pechuga de pavo"]
    },
    2: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Merluza a la plancha con ensalada de rúcula", "Tartar de atún con pepino y zanahoria", "Guiso de verduras con pechuga de pollo", "Tofu salteado con calabacín", "Omelette de vegetales"]
    },
    3: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Pollo a la plancha con puré de coliflor", "Ensalada de quinoa con espárragos", "Filete de pescado con ensalada verde", "Berenjenas rellenas de verduras", "Sopa de calabaza y zanahoria"]
    },
    4: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Tofu al horno con calabacín", "Salmón a la plancha con puré de batata", "Ensalada de espinacas y pimientos", "Guiso de lentejas con verduras", "Arroz integral con verduras salteadas"]
    },
    5: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Tartar de salmón con pepino y aguacate", "Sopa de brócoli y calabacín", "Pechuga de pavo con ensalada de col", "Revuelto de claras con espárragos", "Timbal de quinoa con tomate y pepino"]
    },
    6: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Pollo a la parrilla con verduras asadas", "Guiso de champiñones y espinacas", "Pescado al vapor con espinacas", "Ensalada de rúcula con remolacha", "Omelette de calabacín"]
    },
    7: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Puré de coliflor con pavo asado", "Filete de pescado con ensalada verde", "Guiso de calabacín con zanahoria", "Tofu a la plancha con espárragos", "Batido de espinacas, manzana y jengibre"]
    },
    8: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Pollo al horno con pimientos", "Sopa de calabaza y apio", "Merluza con guarnición de brócoli", "Arroz de coliflor con espárragos", "Tortilla de espárragos y champiñones"]
    },
    9: {
        "Tipo": "Déficit Calórico",
        "Alimentos": ["Ensalada de tomate, espinaca y aguacate", "Crema de espinacas con brócoli", "Filete de pavo con puré de calabaza", "Tofu con ensalada verde", "Pechuga de pollo con ensalada de rúcula"]
    },
    10: {

        "Tipo": "Déficit Calórico",
        "Alimentos": ["Lomo de cerdo magro con puré de zanahorias", "Pimientos rellenos de quinoa", "Sopa de vegetales", "Ensalada de espinacas con remolacha", "Merluza con ensalada de rúcula"]
    },

    #----------------------------------------------------------------------------------------------
    #DIETAS MANTENER ESTADO FISICO
    #----------------------------------------------------------------------------------------------
    11: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Arroz integral con pollo salteado", "Sopa de pollo con verduras", "Ensalada de pasta con atún", "Pechuga de pavo con puré de papa", "Quinoa con espinacas y tomate"]
    },
    12: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Tacos de pescado con aguacate", "Pasta integral con brócoli y pechuga de pollo", "Salmón a la plancha con arroz", "Lentejas con verduras", "Omelette de espinacas y queso fresco"]
    },
    13: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Ensalada de atún con pimientos", "Tallarines de arroz con pollo", "Filete de pescado con puré de papa", "Tofu con brócoli y zanahoria", "Sopa de lentejas con espinacas"]
    },
    14: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Merluza al horno con papas y zanahorias", "Quinoa con verduras", "Guiso de pavo con calabaza", "Ensalada de quinoa con remolacha", "Batido de proteína con frutas"]
    },
    15: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Pasta integral con pollo", "Batido de avena y banana", "Pescado a la plancha con ensalada", "Tortilla de espárragos", "Ensalada de espinacas y nueces"]
    },
    16: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Filete de cerdo con puré de batata", "Calabacines rellenos de pavo", "Ensalada de pasta con vegetales", "Tartar de atún con aguacate", "Lentejas con espinaca"]
    },
    17: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Arroz con pescado y verduras", "Pollo al horno con puré de papa", "Ensalada de rúcula con atún", "Sopa de espinacas", "Pasta integral con salteado de vegetales"]
    },
    18: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Pechuga de pavo con puré de batata", "Tofu con calabacín y pimientos", "Omelette de espinacas y champiñones", "Tallarines con espárragos", "Batido de frutas con avena"]
    },
    19: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Ensalada de arroz integral con pollo", "Sopa de calabaza", "Pechuga de pollo con ensalada de espinaca", "Salmón con puré de papas", "Bowl de quinoa con vegetales"]
    },
    20: {

        "Tipo": "Mantener Estado Físico",
        "Alimentos": ["Arroz con salmón a la plancha", "Guiso de vegetales", "Omelette de jamón y espinacas", "Merluza al horno con brócoli", "Ensalada de rúcula y tomate cherry"]
    },

    #----------------------------------------------------------------------------------------------
    #DIETAS DEFICIT CALORICO
    #----------------------------------------------------------------------------------------------
    21: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Pechuga de pollo con arroz blanco", "Batido de proteína y avena", "Quinoa con pollo y espinacas", "Omelette de jamón y queso", "Salmón con papa al horno"]
    },
    22: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Arroz con carne magra", "Batata con pechuga de pavo", "Tortilla de espinacas y queso", "Salmón con pasta", "Ensalada de quinoa con huevos"]
    },
    23: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Pollo al horno con puré de papa", "Tortilla de clara de huevo con espinacas", "Batido de proteína con frutas", "Arroz integral con carne magra", "Bowl de quinoa"]
    },
    24: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Lomo de cerdo magro con batatas al horno", "Arroz con atún y verduras", "Ensalada de pasta integral con pollo y aguacate", "Pechuga de pavo con puré de batata", "Batido de proteína con leche y plátano"]
    },
    25: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Ensalada de legumbres con quinoa y pollo", "Salmón al horno con papa asada", "Omelette de espinacas, champiñones y queso", "Pasta con carne magra", "Batido de leche con avena y frutas"]
    },
    26: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Pollo con arroz integral y brócoli", "Guiso de lentejas y carne magra", "Pechuga de pavo con puré de papa", "Ensalada de pasta integral con vegetales y atún", "Batido de proteína con leche de almendra"]
    },
    27: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Filete de pescado con puré de batata", "Bowl de arroz con pollo y aguacate", "Tortilla de claras con queso y espinacas", "Pasta integral con pechuga de pollo", "Yogur griego con frutas y nueces"]
    },
    28: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Ternera a la plancha con papas asadas", "Sándwich de pavo y aguacate en pan integral", "Batido de avena con leche y proteína", "Arroz con salmón y espinacas", "Tortilla de jamón y queso con batata"]
    },
    29: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Bowl de quinoa con carne y verduras", "Pechuga de pollo con ensalada de pasta", "Batido de proteínas con leche y fresas", "Guiso de garbanzos con carne magra", "Omelette de huevo y queso con espinacas"]
    },
    30: {

        "Tipo": "Aumentar Masa Muscular",
        "Alimentos": ["Arroz con lomo de cerdo magro y vegetales", "Batido de proteína, plátano y avena", "Tortilla de claras con jamón y espinacas", "Pasta con salsa de tomate y carne magra", "Ensalada de pollo, aguacate y quinoa"]
    }
    }

    

    #----------------------------------------------------------------------------------------------
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
            elif OpcionInformesGenerales=="3":
                ...
            elif OpcionInformesGenerales=="0":
                ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
    guardarDatos('clientes.json', personas)  # Guarda los datos de clientes en el archivo JSON

if __name__ == "__main__":
    main()