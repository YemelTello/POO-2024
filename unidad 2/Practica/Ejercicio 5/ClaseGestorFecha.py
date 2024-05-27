import csv
from ClaseFecha import FechaDeFutbol

class GestorFecha:
    __fechas: list

    def __init__(self):
        self.__fechas = []

    def AgregarFecha(self, unafecha):
        self.__fechas.append(unafecha)

    def ObtenerFechas(self):
        archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 2\\Practica\\Ejercicio 5\\fechasFutbol.csv")
        reader = csv.reader(archivo)
        for fila in reader:
            unafecha = FechaDeFutbol(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
            self.AgregarFecha(unafecha)
        archivo.close()
        return self.__fechas
    
    def getResultados(self):
        lista=[]
        for unpartido in self.__fechas:
            partidoX=[]
            partidoX.append(unpartido.EquipoLocal())
            partidoX.append(unpartido.CantidadGolesL())
            partidoX.append(unpartido.EquipoVisitante())
            partidoX.append(unpartido.CantidadGolesV())
            lista.append(partidoX)
        return lista