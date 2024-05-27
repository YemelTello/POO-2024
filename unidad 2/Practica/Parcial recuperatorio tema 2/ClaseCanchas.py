class Cancha:
    __id: str
    __tipoPiso: str
    __importe:float
    def __init__(self, Id, tipo, importe):
        self.__id = Id
        self.__tipoPiso = tipo
        self.__importe = importe

    def getId(self):
        return self.__id
    
    def getPiso(self):
        return self.__tipoPiso
    
    def getImporte(self):
        return self.__importe
