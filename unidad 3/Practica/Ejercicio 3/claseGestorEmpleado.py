from claseEmpleado import Empleado
import csv

class gestorEmpleado:
    __empleados: list

    def __init__(self):
        self.__empleados = []

    def agregarEmpleado(self, unempleado):
        self.__empleados.append(unempleado)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 3\\empleados.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    unempleado = Empleado(fila[0], int(fila[1]), fila[2])
                    self.agregarEmpleado(unempleado)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")

    def getEmpleados(self):
        return len(self.__empleados)
    
    def getEmpleadoXindice(self, pos):
        return self.__empleados[pos]
    
    def mostrarDuracion(self, ID):
        band = False
        i = 0
        while band is False and i < len(self.__empleados):
            if self.__empleados[i].getID() == ID:
                self.__empleados[i].ListarEmpleado()
                band = True
            else:
                i += 1
        assert band is True, "band no es true xd"

    def mostrarEmpleadoFlojos(self):
        band = False
        for unempleado in self.__empleados:
            if unempleado.getMatriculas() == 0:
                print(unempleado)
                band = True
        assert band is True, "band no es true xd"
