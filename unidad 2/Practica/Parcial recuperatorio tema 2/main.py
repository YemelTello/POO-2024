from ClaseGestorAlquiler import gestorAlquiler
from ClaseGestorCancha import gestorCancha

def menu():
    print("1. Emitir listado")
    print("2. Listar cuanto tiempo en minutos se uso una cancha")
    print("0. SALIR")

    opcion = int(input("Ingrese alguna opcion: "))
    return opcion

def test():
    cancha = gestorCancha()
    alquiler = gestorAlquiler()
    cancha.canchaCSV()
    alquiler.alquilerCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            alquiler.EmitirListado(cancha)

        elif opcion == 2:
            alquiler.contarMinutos()

        else:
            print("Opcion nada que ver bro")
        opcion = menu()

if __name__ == '__main__':
    test()