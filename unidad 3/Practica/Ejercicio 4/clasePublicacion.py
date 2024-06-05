import abc
from abc import ABC

class Publicacion(ABC):
    __titulo: str
    __categoria: str
    __precio: float

    def __init__(self, tit, cat, pr):
        self.__titulo = tit
        self.__categoria = cat
        self.__precio = pr

    def getTitulo(self):
        return self.__titulo
    
    def getCategoria(self):
        return self.__categoria
    
    def getPrecioBase(self):
        return self.__precio
    
    @abc.abstractmethod
    def getImporte(self):
        pass