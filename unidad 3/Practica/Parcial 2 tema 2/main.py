from GestorVehiculos import gestorVehiculos
from classAutobus import Autobous
from classVan import Van

def menu():
    op = None
    try:
        op=int(input("""
                                Menú De Opciones
                [1] Agregar vehiculo
                [2] Ingresate una posicion y veras cosas magicas
                [3] Mostrar la cantidad de vehiculos por tipo
                [4] Mostrar todo sobre los vehiculos
                [0] SALIR
                -> """))
    except ValueError:
        print("Le pifieste al numerin")
    return op

def test():
    gv = gestorVehiculos()
    gv.cargaCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                unvehiculo = int(input("\n\tTipo [1]: AUTOBUS\n \tTipo [2]: VAN\n \t[0]: Salir de esta opcion\n -> "))
                while unvehiculo != 0 and unvehiculo == 1 or unvehiculo == 2:
                    if unvehiculo != 0:
                        marca=input("Ingresa la marca: ")
                        mod=input("Modelo: ")
                        año=int(input("Año de Fabricacion: "))
                        capac=int(input("Capacidad de Pasajeros: "))
                        numP=int(input("Numero de Plazas: "))
                        distance=float(input("Distancia Recorrida: "))
                        tarifa=float(input("Tarifa Base: "))

                        if unvehiculo == 1:
                            tipo = input("Tipo de Servicio: ")
                            turno = input("Turno del Servicio(mañana/tarde/noche): ")
                            tipo, turno = tipo.strip().lower(), turno.strip().lower()
                            nuevoVehiculo = Autobous(marca, mod, año, capac, numP, distance, tarifa, tipo, turno)

                        else:
                            tipoCa = input("Tipo de Carroceria(van/minivan): ").strip().lower()
                            nuevoVehiculo = Van(marca, mod, año, capac, numP, distance, tarifa, tipoCa)
                        gv.agregarVehiculo(nuevoVehiculo)
                        print("VEHICULO AGREGADO")
                    else:
                        print("Ingrese 1 o 2")
                    unvehiculo = int(input("\n\tTipo [1]: AUTOBUS\n \tTipo [2]: VAN\n \t[0]: Salir de esta opcion\n -> "))
                print("SI ESTAS ACA INGRESASTE CUALQUIER COSA O INGRESASTE 0 PARA SALIR, MUY CAPO")
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 2:
            try:
                posicion=int(input("Ingresa la posicion: "))
                gv.MostrarTipoDeV(posicion)
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 3:
            gv.MostrarCuantosHay()

        elif opcion == 4:
            gv.MostrarTodo()
        
        else:
            print("OPCION NADA QUE VER")
        opcion = menu()

if __name__ == "__main__":
    test()