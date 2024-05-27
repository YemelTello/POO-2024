from ClaseGestorTransacción import GestorTransacciones
from ClaseGestorCuenta import GestorCuenta

def menu():
    """Funcion de menu de opciones"""
    opcion = int(input("""
                                 MENÚ DE OPCIONES
          [1] Ingresa DNI para ver datos del cliente
          [2] Ingresa el nuevo "%" anual
          [3] Actualizar saldo
          [4] Ingresar CVU para ver datos
          [5] Almacenar los datos actualizados en un archivo
          [6] Liberar memoria
          [0] SALIR
          -> """))
    return opcion


def test():
    cuenta = GestorCuenta()
    transacción = GestorTransacciones()
    cuenta.leo_csv()
    transacción.leo_csv()
    opcion = menu()
    while opcion != 0:

        if opcion == 1:
            enviarDNI = int(input("Ingrese DNI para ver datos: "))
            obtenerCVU = cuenta.getCVU_desdeMain(enviarDNI)
            if obtenerCVU != -1:
                transacciones = transacción.getCVUTransaccion_DesdeMain(obtenerCVU)
                cuenta.actualizarTransaciones(obtenerCVU, transacciones)
                cuenta.MostrarDatos(obtenerCVU)
            else:
                print("No se encontro el DNI")

        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass

        else:
            print('Opcion Invalida')
        opcion = menu()

if __name__ == '__main__':
    test()