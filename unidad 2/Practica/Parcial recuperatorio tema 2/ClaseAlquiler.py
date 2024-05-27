class Alquiler:
    __nombre: str
    __IdCancha: str
    __horaAlquilada: str
    __minutos: int
    __duracion: int
    def __init__(self, nomb, Id, hora, minu, dura):
        self.__nombre = nomb
        self.__IdCancha = Id
        self.__horaAlquilada = hora
        self.__minutos = minu
        self.__duracion = dura
    
    def getNombre(self):
        return self.__nombre
    
    def getId(self):
        return self.__IdCancha
    
    def getHoras(self):
        return self.__horaAlquilada
    
    def getMinutos(self):
        return self.__minutos
    
    def getDuracion(self):
        return self.__duracion
    
    def __gt__(self, other):
        return self.__horaAlquilada > other.__horaAlquilada