
def archivos():
    archivo = open("datos.txt", 'w')
    archivo.close()

def escribir():
    archivo = open("datos.txt", "a", )

    nombre = raw_input('ingrese nombre: ')
    archivo.write('nombre: ')
    archivo.write(nombre)


    contrasena = raw_input('ingrese contrasena: ')
    archivo.write('\ncontrasena: ')
    archivo.write(contrasena)

    ip = raw_input('ingrese direccion ip: ')
    archivo.write('\ndireccion ip: ')
    archivo.write(ip)

    fecha = raw_input('ingrese fecha inicio de sesion: ')
    archivo.write('\nfecha inicio de sesion: ')
    archivo.write(fecha)

    hora = raw_input('ingrese hora de sesion: ')
    archivo.write('\nhora de sesion: ')
    archivo.write(hora)

'''archivo.write("contrasena: \n")

    archivo.write("direccion ip: \n")
    archivo.write("fecha inicio de sesion: \n")
    archivo.write("hora inicio de sesion: \n")'''

archivos()
escribir()

