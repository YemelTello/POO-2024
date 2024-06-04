from ClaseProgramaCapcitacion import Programa
import csv

class gestorPrograma:
    __programas: list

    def __init__(self):
        self.__programas = []

    def agregarPrograma(self, unprograma):
        self.__programas.append(unprograma)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 3\\capacitacion.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    unprograma = Programa(fila[0], fila[1], int(fila[2]))
                    self.agregarPrograma(unprograma)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")
    
    def getProgramas(self):
        return len(self.__programas)
    
    def getProgramasXindice(self, pos):
        return self.__programas[pos]
    
    def mostrarPrograma(self, nomb):
        band = False
        i = 0
        while band is False and i < len(self.__programas):
            if self.__programas[i].getNombreP() == nomb:
                self.__programas[i].listarEmpleados()
                band = True
            else:
                i += 1
        assert band is True, "band no es true"


