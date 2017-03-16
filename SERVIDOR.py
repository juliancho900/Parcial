# INICIO DEL PROGRAMA

import socket

# crear una variable de conexion tipo socket TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#direccion ip del servidor y puerto de conexion
server.bind(("", 35000))

#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
server.listen(1)

#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
socket_cliente, direccion = server.accept()

# tamano de los mensajes enviados por el cliente

while True:   # esperando conexion

    import menu_servidor

    mensaje_servidor = menu_servidor.menu()
    socket_cliente.send(mensaje_servidor)

    mensaje_cliente = socket_cliente.recv(1024)
    if mensaje_cliente == "fausto":
        print "Usuario Ok"
    else:
        print "usuario incorrecto"

    usuario = socket_cliente.recv(1024)
    if usuario == "luciana":
        print "clave correta"

    else:
        print "clave incorrecta"


    if mensaje_cliente == "julian":
        print "Usuario Ok"
    else:
        print "usuario incorrecto"

    usuario = socket_cliente.recv(1024)
    if usuario == "andres":
        print "clave correta"

    else:
        print "clave incorrecta"



    salir = socket_cliente.recv(1024)
    if salir == "salir":
        break


print str(direccion[0]) + " escribio: ", mensaje_cliente
mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
socket_cliente.send(mensaje_servidor)

# imprimir la direccion ip del cliente str(addr[0])+

print "Hasta Pronto"
socket_cliente.close()
server.close()