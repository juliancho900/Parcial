# INICIO DEL PROGRAMA

import socket
import menu_servidor

cliente = socket.socket()

"""direccion ip del servidor, puerto del servidor, nos conectamos con el metodo connect"""

cliente.connect(("localhost", 35000))

while True:

    mensaje_cliente = raw_input("USUARIO >>: ")
    cliente.send(mensaje_cliente)

    usuario = raw_input("CONTRASENA >>: ")
    cliente.send(usuario)
    print 'BIENVENIDO COMO ADMINISTRADOR'

    mensaje_servidor = cliente.recv(1024)
    menu_servidor.imprimir(mensaje_servidor)

    if mensaje_cliente == "salir":
        break

mensaje_servidor = cliente.recv(1024)
print mensaje_servidor
print "vuelva pronto"

cliente.close()


