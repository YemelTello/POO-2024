from claseLibro import Libro
from claseNodo import Nodo
from claseCD import CD
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getNext()
            return dato
        
    def __getTope(self):
        return self.__tope
    
    def agregarPublicacion(self, unapublicacion):
        nodo = Nodo(unapublicacion)
        nodo.setNext(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
        print("Publicacion nueva cargada!")
    
    def cargaCSV(self):
        try:
            band = False
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 4\\libros.csv")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                if band is False:
                    band = True
                else:
                    unapublicacion = Libro(tit=fila[0],cat=fila[1],pr=float(fila[2]),nomb=fila[3],Fecha=fila[4],cant=int(fila[5]))
                    self.agregarPublicacion(unapublicacion)
            archivo.close()
        except FileNotFoundError:
            print("NOSE LEER LIBROS")
        try:
            bandera = False
            archi = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 4\\cd.csv")
            reader = csv.reader(archi, delimiter=";")
            for filita in reader:
                if bandera is False:
                    bandera = True
                else:
                    unapubli = CD(tit=filita[0],cat=filita[1],pr=float(filita[2]),time=int(filita[3]),narra=filita[4])
                    self.agregarPublicacion(unapubli)
            archivo.close()
        except FileNotFoundError:
            print("NOSE ESCUCHAR AUDIO-LIBROS")

    def getPublicacion(self, pos):
        if pos < self.__getTope():
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getNext()
            if isinstance(aux.getDato(), CD):
                print(f'{aux.getDato().getTitulo()} es un CD')
            elif isinstance(aux.getDato(), Libro):
                print(f'{aux.getDato().getTitulo()} es un Libro')
        else:
            print(f"Posicion invalida, tiene que ser entre 0 y ", self.__getTope()-1)

    def mostrarCant(self):
        cont = 0
        sumo = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), Libro):
                cont += 1
            elif isinstance(aux.getDato(), CD):
                sumo += 1
            aux = aux.getNext()
        print(f"Hay {cont} Libros y {sumo} CD's")
    
    def mostrarTodo(self):
        for publi in self:
            importe = publi.getImporte()
            print(f"Titulo: {publi.getTitulo()}\n Categoria: {publi.getCategoria()}\n Valor: {round(importe,2)}")