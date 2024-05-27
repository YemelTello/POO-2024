from ClaseGestorCabaña import GestoCabaña
from ClaseGestorReserva import GestorReserva


def menu():
    opcion = int(input("""
                                 MENÚ DE OPCIONES
          [1] Mostrar cabañas disponibles
          [2] Listar reservas por fecha
          [0] SALIR
          -> """))
    return opcion


def test():
    cabaña = GestoCabaña()
    reserva = GestorReserva()
    cabaña.AlmacenarCabañaCSV()
    reserva.AlmacenarReservaCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            cabaña.cabanasDisponibles(reserva)

        elif opcion == 2:
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            hay_reservita = reserva.HAY_reserva(fecha)
            if hay_reservita:
                print(f"Reserva para la fecha:  {fecha}")
                print("N° de cabaña   Importe diario   Cantidad días   Seña   Importe a cobrar")
                reserva.listado_reservas(cabaña, fecha)

        else:
            print('Opcion Invalida')
        opcion = menu()

if __name__ == '__main__':
    test()