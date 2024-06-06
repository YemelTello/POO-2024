from classAutobus import Autobous
from classVan import Van
import csv

class gestorVehiculos:
    __vehiculos: list

    def __init__(self):
        self.__vehiculos = []

    def agregarVehiculo(self, unvehiculo):
        self.__vehiculos.append(unvehiculo)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Parcial 2 tema 2\\vehiculos.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    if fila[0] == "A":
                        unvehiculo = Autobous(fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9])
                        self.agregarVehiculo(unvehiculo)
                    elif fila[0] == "V":
                        unvehiculo = Van(fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8])
                        self.agregarVehiculo(unvehiculo)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")

    def MostrarTipoDeV(self, pos):
        try:
            if pos < len(self.__vehiculos):
                if isinstance(self.__vehiculos[pos], Autobous):
                    print("SOY UN AUTOBUSSSSSSSSSSSS")
                elif isinstance(self.__vehiculos[pos], Van):
                    print("SOY UNA VANNNNNNNNNNNNNNN")
        except IndexError:
            print("La posicion no puede ser mayor al de la fila, pruebe con un numero mas chico")

    def MostrarCuantosHay(self):
        cont = 0
        sumo = 0
        for vehiculo in self.__vehiculos:
            if isinstance(vehiculo, Autobous):
                cont += 1
            elif isinstance(vehiculo, Van):
                sumo += 1
        print(f"Hay {cont} Autobus/es")
        print(f"Hay {sumo} Van/s")
        
    def MostrarTodo(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)