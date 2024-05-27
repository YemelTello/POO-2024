from ClaseCabaña import Cabaña
import csv
import numpy as np

class GestoCabaña:
    __cabañas: np.ndarray
    __contador = 0
    __dimension = 11
    __incremento = 1

    def __init__(self):
        self.__cabañas = np.empty(self.__dimension, dtype=Cabaña)

    def AgregarCabaña(self, unacabaña):
        if self.__contador == self.__dimension:
            print("Se solicito espacio")
            self.__dimension += self.__incremento
            self.__cabañas.resize(self.__dimension)
        self.__cabañas[self.__contador] = unacabaña
        self.__contador += 1
    
    def AlmacenarCabañaCSV(self):
        archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 2\\Practica\\Parcial recuperatorio tema 1\\Cabañas.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                unacabaña = Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
                self.AgregarCabaña(unacabaña)
        archivo.close()
        return self.__cabañas

    def cabanasDisponibles(self, reservas):
        huespedes=int(input("Ingrese numero de Huespedes\n"))
        for cab in self.__cabañas:
            band=False
            if cab >= huespedes and reservas.HAY_reserva(cab.getNumC()) is False:
                print(f"La Cabaña Numero {cab.getNumC()} Esta disponible para {huespedes} personas\n")
                band=True
        if band==False:
            print("No hay cabañas disponibles\n")

    def importe_diario(self,num_cab):
        i=0
        while i < len(self.__cabañas) and self.__cabañas[i].getNumC() != num_cab:
            i+=1
        return self.__cabañas[i].getImpo()