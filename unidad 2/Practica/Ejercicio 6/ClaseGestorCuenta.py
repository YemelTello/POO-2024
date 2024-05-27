from ClaseCuenta import Cuenta
import numpy as np
import csv

class GestorCuenta:
    __contador: int
    __dimension: int
    __incremento: int
    __cuentas: np.ndarray

    def __init__(self):
        self.__contador = 0
        self.__dimension = 0
        self.__incremento = 5
        self.__cuentas = np.empty(self.__dimension, dtype = Cuenta)

    def AgregarCuenta(self, unacuenta):
        if self.__contador == self.__dimension:
            self.__dimension += self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__contador] = unacuenta
        self.__contador += 1

    def leo_csv(self):
        archivo = open('cuentasBilletera.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader: 
            self.AgregarCuenta(Cuenta(fila[0],fila[1],int(fila[2]),int(fila[3]),float(fila[4]),int(fila[5])))
        archivo.close()

    def getCVU_desdeMain(self, dni):
        long = self.__contador
        i = 0
        bandera = False
        print(type(dni))
        while bandera is False and i < long:
            if dni == self.__cuentas[i].getDNI():
                cvu = self.__cuentas[i].getCVUc()
                bandera = True
            else:
                i += 1
        if bandera is False:
            return -1
        else:
            return cvu


        
    def actualizarTransaciones(self, cvu, transacciones):
        i = 0
        long = self.__contador
        bandera = False
        while bandera is False and i < long:
            if cvu == self.__cuentas[i].getCVUc():
                self.__cuentas[i].actualizarSaldo_Transaccion(transacciones)
                bandera = True
            else:
                i += 1
        print(f"Se actualizo el saldo de: {self.__cuentas[i].getCVUc()} con sus transacciones")

    def MostrarDatos(self, cvu):
        i = 0
        long = self.__contador
        bandera = False
        while bandera is False and i < long:
            if cvu == self.__cuentas[i].mostrarDatos():
                bandera = True
            else:
                i += 1