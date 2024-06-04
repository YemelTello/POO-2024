from claseLadrillos import Ladrillo
import csv
import random

class gestorLadrillo:
    __ladrillos: list

    def __init__(self):
        self.__ladrillos = []
    
    def agregarLadrillos(self, unladrillo):
        self.__ladrillos.append(unladrillo)

    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 2\\ladrillos.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    unladrillo = Ladrillo(int(fila[0]),int(fila[1]), float(fila[2]), float(fila[3]))
                    self.agregarLadrillos(unladrillo)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER")

    def asignarMateriales(self,GM):
        indicesLadrillos = list(range(len(self.__ladrillos))) 
        indicesMateriales = list(range(GM.getTotalMateriales())) 
        for i in range(4):
            indiceRandomL = random.choice(indicesLadrillos)  
            indiceRandomM = random.choice(indicesMateriales)
            self.__ladrillos[indiceRandomL].agregarMaterial(GM.getMaterialesXposicion(indiceRandomM))

    def mostrarLadrillos(self, xID):
        band = False
        i = 0
        while band is False and i < len(self.__ladrillos):
            if self.__ladrillos[i].getId() == xID:
                self.__ladrillos[i].ListarCostoyCaracteristicas()
                band = True
            else:
                i += 1
        assert band is True, "band no es true xd"

    def mostrarTotal(self):
        for unladrillo in self.__ladrillos:
            print(f"Ladrillo {unladrillo.getId()} -> Costo Total De Fabricacion: ",unladrillo.getCostoTotal())

    def mostrarFabricados(self):
        print("\tN° Identificador \tMaterial \t\tCosto asociado")
        for unladrillo in self.__ladrillos:
            xid = unladrillo.getId()
            xmat = unladrillo.getMateriales()
            if xmat != "":
                xcosto = unladrillo.getCostosAdicionales()
                print(f"""
                {xid}                      {xmat}                           {xcosto}
                      """)
            else:
                print(f"""
                {xid}                      -                                -""")