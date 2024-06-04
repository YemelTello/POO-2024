from claseMaterialRefractario import Material
import csv

class gestorMaterial:
    __materiales: list

    def __init__(self):
        self.__materiales = []

    def agregarMateriales(self, unmaterial):
        self.__materiales.append(unmaterial)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 2\\materiales.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    unmaterial = Material(int(fila[0]), fila[1], float(fila[2]), float(fila[3]))
                    self.agregarMateriales(unmaterial)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")
    
    def getTotalMateriales(self):
        return len(self.__materiales)
    
    def getMaterialesXposicion(self, pos):
        return self.__materiales[pos]