from GestorClientes import gestorC
from GestorMovimientos import gestorM

def menu():
    print("1.")
    print("2.")
    print("3.")
    print("4.")

    opcion = int(input("Ingrese alguna opcion: "))
    return opcion

def test():
    cliente = gestorC()
    movimiento = gestorM()
    cliente.ObtenerClienteCSV()
    movimiento.ObtenerMovimientoCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            cliente.ListaDatos(movimiento)
        elif opcion == 2:
            cliente.ClienteTuvoMovimiento(movimiento)
        elif opcion == 3:
            movimiento.OrdenamientoCuenta()
        else:
            print("Opcion nada que ver bro")
        opcion = menu()

if __name__ == '__main__':
    test()