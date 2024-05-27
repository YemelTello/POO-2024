import csv
import numpy as np
from ClaseCanchas import Cancha

class gestorCancha:
    __cancha: np.ndarray
    __contador = 0
    __dimension = 7
    __incremento = 1

    def __init__(self):
        self.__cancha = np.empty(self.__dimension, dtype=Cancha)

    def agregarCancha(self, unacancha):
        if self.__contador == self.__dimension:
            print("se solicita espacio")
            self.__dimension += self.__incremento
            self.__cancha.resize(self.__dimension)
        self.__cancha[self.__contador] = unacancha
        self.__contador += 1

    def canchaCSV(self):
        archivo = open("Canchas.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                unacancha = Cancha(fila[0], fila[1], float(fila[2]))
                self.agregarCancha(unacancha)
        archivo.close()
        return self.__cancha

    def ImporteXhora(self, Id):
        i = 0
        while self.__cancha[i].getId() != Id:
            i += 1
        return self.__cancha[i].getImporte()