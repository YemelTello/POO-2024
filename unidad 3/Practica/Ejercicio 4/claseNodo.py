from clasePublicacion import Publicacion

class Nodo:
    __publicacion: Publicacion
    __next: object

    def __init__(self, publi):
        self.__publicacion = publi
        self.__next = None

    def setNext(self, siguiente):
        self.__next = siguiente

    def getNext(self):
        return self.__next

    def getDato(self):
        return self.__publicacion