class Material:
    __material: int
    __caracteristicas: str
    __cantUtilizada: float
    __costoAdicional: float

    def __init__(self, mat, carac, cant, costo):
        self.__material = mat
        self.__caracteristicas = carac
        self.__cantUtilizada = cant
        self.__costoAdicional = costo

    def getMaterial(self):
        return self.__material
    
    def getCaracteristicas(self):
        return self.__caracteristicas
    
    def getCantidad(self):
        return self.__cantUtilizada
    
    def getCosto(self):
        return self.__costoAdicional