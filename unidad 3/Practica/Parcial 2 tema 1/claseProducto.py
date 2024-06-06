from abc import ABC
import abc

class Producto(ABC):
    __nombre: str
    __fechaEnv: str
    __fechVenc: str
    __temperatura: float
    __pais: str
    __numLote: int
    __costoBase: float

    def __init__(self, nomb, fechaE, fechaV, temp, pais, num, costo):
        self.__nombre = nomb
        self.__fechaEnv = fechaE
        self.__fechVenc = fechaV
        self.__temperatura = temp
        self.__pais = pais
        self.__numLote = num
        self.__costoBase = costo

    def __str__(self):
        return f"\n \tNombre de Producto: {self.getNombre()}\n \tPaís de Origen: {self.getPais()}\n \tTemperatura de mantenimiento recomendad {self.getTemparatura()}\n \tImporte: {self.getImporteDeVenta()}"

    def getNombre(self):
        return self.__nombre
    
    def getFechaEnvasado(self):
        return self.__fechaEnv
    
    def getFechaVencimiento(self):
        return self.__fechVenc
    
    def getTemparatura(self):
        return self.__temperatura
    
    def getPais(self):
        return self.__pais
    
    def getNumero(self):
        return self.__numLote
    
    def getCostoBase(self):
        return self.__costoBase
    
    @abc.abstractmethod
    def getImporteDeVenta(self):
        pass