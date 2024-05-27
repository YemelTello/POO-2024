import csv
from ClaseEquipo import Equipo


class GestorEquipo:
    __equipos: list

    def __init__(self):
        self.__equipos = []

    def agregarEquipo(self, unequipo):
        self.__equipos.append(unequipo)

    def obtenerEquiposCsv(self):
        archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 2\\Practica\\Ejercicio 5\\equipos2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            unEquipo = Equipo(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]))
            self.agregarEquipo(unEquipo)
        archivo.close()

    def calcularPuntos(self, GolesF, GolesC):
        if GolesF > GolesC:
            return 3
        elif GolesF == GolesC:
            return 1
        else:
            return 0


    def obtenerEquipoListado(self, fechas, EquipoElejido):
        equipo_encontrado = False
        for equipo in self.__equipos:
            if equipo.MNombre() == EquipoElejido:
                equipo_encontrado = True
                print("Equipo:", EquipoElejido)
                print("Fecha      Goles a Favor  Goles en Contra  Diferencia de Goles  Puntos")
                for f in fechas.ObtenerFechas():
                    if equipo.ID() == f.EquipoLocal():
                        puntos = self.calcularPuntos(f.CantidadGolesL(), f.CantidadGolesV())
                        diferencia_goles = f.CantidadGolesL() - f.CantidadGolesV()
                        print("{}     {}               {}                 {}                     {}".format(f.Fecha(), f.CantidadGolesL(), f.CantidadGolesV(), diferencia_goles, puntos))
                    elif equipo.ID() == f.EquipoVisitante():
                        puntos = self.calcularPuntos(f.CantidadGolesV(), f.CantidadGolesL())
                        diferencia_goles = f.CantidadGolesV() - f.CantidadGolesL()
                        print("{}     {}               {}                 {}                     {}".format(f.Fecha(), f.CantidadGolesV(), f.CantidadGolesL(), diferencia_goles, puntos))
                print("Totales: {}         {}        {}            {}" .format(equipo.GolesF(), equipo.GolesC(), equipo.diferencia(), equipo.Puntos()))

        if equipo_encontrado is False:
            print("No se encontró el equipo:", EquipoElejido)

    def ActualizarLista(self, resultados):
        for equipo in self.__equipos:
            for resultado in resultados:
                if equipo.ID() == resultado[0]:
                    equipo.GolesF += resultado[1]
                    equipo.GolesC += resultado[3]
                    equipo.diferencia += (resultado[1] - resultado[3])
                    if resultado[1] > resultado[3]:
                        Puntos = 3
                    elif resultado[1] == resultado[3]:
                        Puntos = 1
                    else:
                        Puntos = 0
                    equipo.Puntos += Puntos
                elif equipo.ID() == resultado[2]:
                    equipo.GolesF += resultado[3]
                    equipo.GolesC += resultado[1]
                    equipo.diferencia += (resultado[3] - resultado[1])
                    if resultado[3] > resultado[1]:
                        Puntos = 3
                    elif resultado[3] == resultado[1]:
                        Puntos = 1
                    else:
                        Puntos = 0
                    equipo.Puntos += Puntos
        print("LISTA ACTUALIZADA")
        # Devolver una lista de listas con los datos de los equipos actualizados
        return [[equipo.MNombre(), equipo.GolesF(), equipo.GolesC(), equipo.diferencia(), equipo.Puntos()] for equipo in self.__equipos]

    def __gt__(self, unEquipo):
        if self.Puntos() > unEquipo.Puntos():
            return True
        elif self.Puntos() == unEquipo.Puntos():
            if self.diferencia() > unEquipo.diferencia():
                return True
            elif self.diferencia() == unEquipo.diferencia():
                return self.GolesF() > unEquipo.GolesF()
        return False

    def OrdenarTabla(self):
        self.__equipos.sort(key=lambda equipo: equipo.Puntos(), reverse=True)
        print("Tabla de posiciones ordenada")

    def guardarCSV(self, resultados):
        posiciones = self.ActualizarLista(resultados)
        archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 2\\Practica\\Ejercicio 5\\tposiciones.csv", mode='w', newline='')
        writer = csv.writer(archivo, delimiter=";")
        for fila in posiciones:
            writer.writerow(fila)
        archivo.close()
        print("Se guardaron los datos exitosamente!")