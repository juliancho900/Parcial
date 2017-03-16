# -*- coding: utf-8 -*-
import time
from _socket import socket

def main():

    ''' Esto es una documentación de función'''
    server = socket()
    server.connect(("localhost", 35000))



    while True:
        #Enviar mensaje cliente
        mensaje_cliente = raw_input(">> ")

        if mensaje_cliente:
            try:
                server.send(mensaje_cliente)
            except TypeError:
                server.send(bytes(mensaje_cliente,"utf-8"))
        # Respuesta Servidor
        mensaje_servidor = server.recv(1024)
        if mensaje_servidor:
            print mensaje_servidor

if __name__ == '__main__':
    main()
