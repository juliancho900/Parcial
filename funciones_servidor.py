# -*- coding: utf-8 -*-
import json

def menu():
    lista = ["Bienvenido", "1. Crear Peliculas", "2.Eliminar Pelicula", "3.listar pelicula", "4.Ver peliculas vendidas", "5.sillas disponibles"]
    cadena = json.dumps(lista)
    return cadena
def getnum_1():
    lista = ["Ingese la opcion 1 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def getnum_2():
    lista = ["Ingese la opcion 2 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def getnum_3():
    lista = ["Ingese la opcion 3 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def getnum_4():
    lista = ["Ingese la opcion 4 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena
def getnum_5():
    lista = ["Ingese la opcion 5 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def archivo():
    lista = ["Ingese el nombre del archivo y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def crear_txt(nombreFichero):
    archivo = str(nombreFichero + ".txt")
    lista = ["Archivo = " + archivo,
             "Creado Exitosamente , Ingrese 0  y presione enter para volver al menu "]
    cadena = json.dumps(lista)
    archivo = open(archivo, 'jyf')
    archivo.close()
    return cadena