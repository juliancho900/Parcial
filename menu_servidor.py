import json

def menu():
    lista = ["cinema", "1. crear peliculas", "2. eliminar peliculas", "3. listar peliculas", "4. ver peliculas vendidas", "5. sillas disponibles vendidas", "Digite el numero de la opcion >>"]
    cadena = json.dumps(lista)
    return cadena


def imprimir(cadena):
    lista = json.loads(cadena)
    for i in lista:
        print i

#def iniciar_sesion():
 #   pass


def usuario():
     lista = ["Ingrese su Usuario >>"]
     cadena = json.dumps(lista)
     return cadena

def contrasena():
    lista = ["Ingrese su Contrasena >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario(cadena):
     if(cadena == "fausto"):
         return True
     else:
         return False

def validar_contrasena(cadena):
    if(cadena == "luciana"):
        return True
    else:
        return False

def usuario_error():
    lista = ["Usuario incorrecto", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def contrasena_error():
    lista = ["Contrasena incorrecta", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def getmenu_error():
    lista = ["Opcion Invalida", "\n", "Presione enter para mostrar el menu de nuevo"]
    cadena = json.dumps(lista)
    return cadena

def num_1():
    lista = ["Ingese el numero 1 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def num_2():
    lista = ["Ingese el numero 2 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def suma(num1, num2):
    suma = str(num1 + num2)
    lista = ["Resultado de la operacion = " + suma, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena