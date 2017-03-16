# -*- coding: utf-8 -*-
from socket import socket, error
from threading import Thread
from time import sleep
import time
import funciones_servidor

class Cliente(Thread): # Extender clase Thread, Herencia
    ''' Función que Genera Hilos '''
    def __init__(self, con, dire): # Constructor
        Thread.__init__(self) # Hereda de la clase Thread, Instancia la clase y corre el constructor
        self.conexion   = con
        self.direccion  = dire

    def run(self): # Corredor
        while True:
            try:
                mensaje_cliente = self.conexion.recv(1024)
                mensaje_cliente = funciones_servidor.menu()
            except error:
                print("[%s] Error de Lectura " %self.name) #%s => String, self.name => Variable de error
                break
            else:
                if mensaje_cliente:
                    self.conexion.send(mensaje_cliente)
                if mensaje_cliente == 'salir':
                    self.hora_fin = time.time()
                    tiempo = self.hora_fin - hora_inicio
                    print tiempo

def main():

    server = socket()
    server.bind(("localhost",35000))
    server.listen(1)
    while True:
        con, dire = server.accept()
        hilo = Cliente(con,dire)
        hilo.start()
        hora_inicio = time.time()
        #hora_final al desconectar el cliente
        print("%s:%d conexion de " %dire)

if __name__ == '__main__':
    main()


