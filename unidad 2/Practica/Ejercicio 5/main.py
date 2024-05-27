from ClaseGestorEquipo import GestorEquipo
from ClaseGestorFecha import GestorFecha

def menu():
    """Funcion de menu de opciones"""
    op = int(input("""
                                 MENÚ DE OPCIONES
          [1] Leer datos de equipos desde csv
          [2] Leer datos de fechas desde csv
          [3] Ingresa nombre del equipo para ver datos
          [4] Actualizar tabla despues de jugar fechas
          [5] Ordenar tabla
          [6] Guardar tabla ordenada en un csv
          [0] SALIR
          -> """))
    return op


def test():
    equipos = GestorEquipo()
    fechas = GestorFecha()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            equipos.obtenerEquiposCsv()
            print("Operacion 1 joyita!")
        elif opcion == 2:
            fechas.ObtenerFechas()
            print("Operacion 2 joyita!")
        elif opcion == 3:
            EquipoElejido = input("Ingrese nombre de equipo: ")
            equipos.obtenerEquipoListado(fechas, EquipoElejido)
            print("Operacion 3 joyita!")
        elif opcion == 4:
            resultados = fechas.getResultados()
            equipos.ActualizarLista(resultados)
            equipos.obtenerEquipoListado(fechas, EquipoElejido)
            print("Operacion 4 joyita!")
        elif opcion == 5:
            equipos.OrdenarTabla()
            print("Operacion 5 joyita!")
        elif opcion == 6:
            equipos.guardarCSV(resultados)
            print("Operacion 6 joyita!")
        else:
            print("Opcion joyita'nt")
        opcion = menu()

if __name__ == '__main__':
    test()