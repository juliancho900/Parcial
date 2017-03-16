def suma():
    opc = int(input("Selecione una Opcion >>: "))
    while (opc == 1):
        print 'Eligio Suma'

        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese Otro Numero: \n"))
        if (opc == 1):
            print "La Suma es: ", x+y
            return suma()
suma()


def resta():

    opc = int(input("Selecione una Opcion: "))
    while (opc == 2):
        print 'Eligio Resta'

        x = int(input("Ingrese Numero: \n"))
        y = int(input("Ingrese Otro Numero: \n"))
        if (opc == 2):
            print "La Resta es: ", x-y
            return resta()
resta()


def producto():
    opc = int(input("Selecione una Opcion: "))
    while (opc == 3):
        print 'Eligio Multiplicacion'

        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese Otro Numero: \n"))
        if (opc == 3):
            print "El producto es: ", x * y
            return


producto()


def division():
    opc = int(input("Selecione una Opcion: "))
    while (opc == 4):
        print 'Eligio Division'

        x = int(input("Ingrese un Numero: \n"))
        y = int(input("Ingrese Otro Numero: \n"))
        if (opc == 4):
            try:
                print "La division es: ", x / y
            except ZeroDivisionError:
                print "No se Permite la Division Entre 0"

division()

