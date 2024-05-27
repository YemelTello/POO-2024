from ClaseMovimiento import Movimiento
import numpy as np
import csv

class gestorM:
    __movimientos: np.ndarray
    __contador = 0
    __dimension = 21
    __incremento = 3

    def __init__(self):
        self.__movimientos = np.empty(self.__dimension, dtype=Movimiento)
        
    def AgregarMovimiento(self, unMovimiento):
        if self.__contador == self.__dimension:
            print("Se solicito espacio")
            self.__dimension += self.__incremento
            self.__movimientos.resize(self.__dimension)
        self.__movimientos[self.__contador] = unMovimiento
        self.__contador += 1
        
    def ObtenerMovimientoCSV(self):
        archivo = open("MovimientosAbril2024.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                #print("", fila)
                unMovimiento = Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]))
                self.AgregarMovimiento(unMovimiento)
        archivo.close()
    
    def OrdenamientoCuenta(self):
        self.__movimientos = np.sort(self.__movimientos)
        print ("La lista se ordeno Correctamente")
        for i in range(len(self.__movimientos)):
            print(self.__movimientos[i].getNro())
