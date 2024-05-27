from ClaseCliente import Cliente
from ClaseMovimiento import Movimiento

import csv

class gestorC:
    __cliente: list
    
    def __init__(self):
        self.__cliente = []
        
    def AgregarCliente(self, unCliente):
        self.__cliente.append(unCliente)

    def ObtenerClienteCSV(self):
        archivo = open("ClientesFarmaCiudad.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                unCliente = Cliente(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4]))
                self.AgregarCliente(unCliente)
        archivo.close()

    def BuscaDNI(self, xdni):
        indice = 0
        ValorRetorno = None
        bandera = False
        while not bandera and indice < len(self.__cliente):
            if int(self.__cliente[indice].getDNI()) == int(xdni):
                print("DNI ENCONTRADO")
                bandera = True
                ValorRetorno = indice
            indice += 1
        return ValorRetorno
    
    def ListaDatos(self, m):
        xdni = int(input("Ingrese DNI del cliente para mostrar: \n"))
        pos = self.BuscaDNI(xdni)
        j = 0
        print ("DNI ES IGUAL")
        saldoactualizado = 0
        if pos is not None:
            print("CLIENTE: {} {}                    NUMERO DE CUENTA: {}\n".format(self.__cliente[pos].getNombre(),self.__cliente[pos].getApellido(),self.__cliente[pos].getCuenta()))
            print("SALDO ANTERIOR: ${}\n".format(self.__cliente[pos].getSaldo()))
            print("MOVIMIENTOS\n")
            print("FECHA                        DESCRIPCION                IMPORTE               TIPO MOVIMIENTO")
            while j < m._gestorM__contador:
                if int(self.__cliente[pos].getCuenta()) == int(m._gestorM__movimientos[j].getNro()):
                    print("{:>5}{:>31}{:>21}{:>21}".format(m._gestorM__movimientos[j].getFecha(),m._gestorM__movimientos[j].getDescripcion(),m._gestorM__movimientos[j].getImporte(),m._gestorM__movimientos[j].getTipo()))
                    if str(m._gestorM__movimientos[j].getTipo()) == 'P':    
                        saldoactualizado -= float(m._gestorM__movimientos[j].getImporte())
                    else: 
                        saldoactualizado += float(m._gestorM__movimientos[j].getImporte())
                j += 1
        print("------------------------------------------------------------------\n")
        print("SALDO ACTUALIZADO: ${} ".format(float(saldoactualizado) + float(self.__cliente[pos].getSaldo())))

    def ClienteTuvoMovimiento(self,m):
        xdni = int(input("Ingrese DNI del cliente para mostrar: \n"))  
        pos = self.BuscaDNI(xdni)
        i = 0
        bandera = False
        while i < m._gestorM__contador:
            if int(self.__cliente[pos].getCuenta()) == int(m._gestorM__movimientos[i].getNro()):
                bandera = True
            i += 1
        if bandera:
            print("El cliente {} {} tuvo al menos un movimiento en el mes".format(self.__cliente[pos].getNombre(),self.__cliente[pos].getApellido()))
        else:
            print("El cliente no tuvo movimientos")
            