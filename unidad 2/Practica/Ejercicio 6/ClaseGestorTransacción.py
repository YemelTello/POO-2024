from ClaseTransacción import Transacciones
import csv

class GestorTransacciones:
    __transacciones: list

    def __init__(self):
        self.__transacciones = []

    def agregarTransaccion(self,unatransaccion):
        self.__transacciones.append(unatransaccion)

    def leo_csv(self):
        archivo= open('transaccionesBilletera.csv')
        reader= csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera is True:
                bandera = False
            else:
                self.agregarTransaccion(Transacciones(int(fila[0]),int(fila[1]),float(fila[2]),fila[3]))
        archivo.close()

    def getCVUTransaccion_DesdeMain(self, cvu):
        acum = 0
        for unatransaccion in self.__transacciones:
            if unatransaccion.getCVUt() == cvu:
                acum += unatransaccion.getImporte()
        return acum