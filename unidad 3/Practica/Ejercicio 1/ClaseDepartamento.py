class Departamento:
    __IdDpto: int
    __IdEdi: int
    __NomyApe: str
    __NumeroPiso: int
    __NumeroDpto: int
    __CantHabitaciones: int
    __CantidadBaños: int
    __Superficie: float

    def __init__(self, idD, idE, nomb, numpi, numdpt, canth, cantb, sup):
        self.__IdDpto = idD
        self.__IdEdi = idE
        self.__NomyApe = nomb
        self.__NumeroPiso = numpi
        self.__NumeroDpto = numdpt
        self.__CantHabitaciones = canth
        self.__CantidadBaños = cantb
        self.__Superficie = sup
        
    def __str__(self):
        return f"ID Depto: {self.__IdDpto}\nNombre Propietario: {self.__NomyApe}\nCantidad Baños: {self.__CantidadBaños}\nCantidad Habitaciones: {self.__CantHabitaciones}\n"
    
    def getIdDpto(self):
        return self.__IdDpto
    
    def getIdEdi(self):
        return self.__IdEdi
    
    def getNombre(self):
        return self.__NomyApe
    
    def getNumPiso(self):
        return self.__NumeroPiso
    
    def getNumDpto(self):
        return self.__NumeroDpto
    
    def getHabitaciones(self):
        return self.__CantHabitaciones
    
    def getBaños(self):
        return self.__CantidadBaños
    
    def getSuperficie(self):
        return self.__Superficie