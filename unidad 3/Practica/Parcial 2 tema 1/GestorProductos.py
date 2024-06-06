from claseRefrigerados import Refrigerados
from claseCongelados import Congelados
import csv

class gestorProducto:
    __productos: list

    def __init__(self):
        self.__productos = []

    def agregarProducto(self, unproducto):
        self.__productos.append(unproducto)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Parcial 2 tema 1\\productos.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    if fila[0] == "R":
                        unproducto = Refrigerados(fila[1], fila[2], fila[3], float(fila[4]), fila[5], fila[6], float(fila[7]), fila[8])
                        self.agregarProducto(unproducto)
                    elif fila[0] == "C":
                        unproducto = Congelados(fila[1], fila[2], (fila[3]), float(fila[4]), fila[5], fila[6], float(fila[7]), fila[8], fila[9])
                        self.agregarProducto(unproducto)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")

    def MostrarPosicion(self, pos):
        if pos < len(self.__productos):
            if isinstance(self.__productos[pos], Refrigerados):
                print("SOY UN PRODUCTO REFRIGERADO")
            elif isinstance(self.__productos[pos], Congelados):
                print("SOY UN PRODUCTO CONGELADO")
        else:
            print("Ingrese un numero mas bajito")

    def MostrarCadaTipo(self):
        contR = 0
        contC = 0
        for producto in self.__productos:
            if isinstance(producto, Refrigerados):
                contR += 1
            elif isinstance(producto, Congelados):
                contC += 1
        print(f"Hay {contR} producto/s Refrigerado/s y hay {contC} producto/s Congelado/s")

    def MostrarTodo(self):
        for producto in self.__productos:
            print(producto)