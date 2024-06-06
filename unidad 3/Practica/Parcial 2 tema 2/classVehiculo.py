import abc
from abc import ABC

class Vehiculo(ABC):
    __marca: str
    __modelo: str
    __añoDeFabricacion: int
    __capacidad: int
    __numeroDePlazas: int
    __distanciaRecorrida: float
    __tarifaBase: float

    def __init__(self, marca, mod, año, capac, numP, distance, tarifa):
        self.__marca = marca
        self.__modelo = mod
        self.__añoDeFabricacion = año
        self.__capacidad = capac
        self.__numeroDePlazas = numP
        self.__distanciaRecorrida = distance
        self.__tarifaBase = tarifa

    def __str__(self):
        return f"\n \tModelo: {self.getModelo()}\n \t Año de fabricación: {self.getAño()}\n \t Capacidad de pasajeros: {self.getCapacidad()}\n \t Tarifa: {self.getTarifaDeServicios()}"
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAño(self):
        return self.__añoDeFabricacion
    
    def getCapacidad(self):
        return self.__capacidad
    
    def getNumeroDePlazas(self):
        return self.__numeroDePlazas
    
    def getDistancia(self):
        return self.__distanciaRecorrida
    
    def getTarifaBase(self):
        return self.__tarifaBase
    
    @abc.abstractmethod
    def getTarifaDeServicios(self):
        pass