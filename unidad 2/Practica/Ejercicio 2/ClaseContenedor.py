from ClaseCajaAhorro import CajaAhorro

__const: CajaAhorro

def ObtenerDatos(self, Cuil):
    for Cuil in self.__cuil:
        print("Nombre: {}, apellido: {}, saldo: {}" .format(self.__nombre, self.__apellido, self.__saldo))

def AgregarDatos(self, nombre, apellido, saldo, cuil):
    bandera = input("Escriba 1 si quiere ingresar mas datos, sino 0")
    while bandera != '0':   
            print(input("Ingrese nombre"))  
            print(input("Ingrese apellido"))    
            print(input("Ingrese saldo"))   
            print(input("Ingrese cuil"))

            self.__nombre = nombre
            self.__apellido = apellido
            self.__saldo = saldo
            self.__cuil = cuil

            bandera = input("Escriba 1 si quiere ingresar mas datos, sino 0")