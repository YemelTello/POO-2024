class Cabaña:
    __numero: int
    __cantHabit: int
    __camasG: int
    __camasC: int
    __importeXdia: float

    def __init__(self, num, hab, grande, chica, importe):
        self.__numero = num
        self.__cantHabit = hab
        self.__camasG = grande
        self.__camasC = chica
        self.__importeXdia = importe

    def getNumC(self):
        #retorna el numero de la cabaña
        return self.__numero
    
    def getCantHabi(self):
        #retorna la cantidad de habitaciones que hay en la cabaña
        return self.__cantHabit
    
    def getCamasG(self):
        #retorna la cantidad de camas grandes que hay en la cabaña
        return self.__camasG
    
    def getCamasC(self):
        #retorna la cantidad de camas chicas que hay en la cabaña
        return self.__camasC
    
    def getImpo(self):
        #retorna lo que vale reserva al cabaña
        return self.__importeXdia
    
    def __ge__(self, other):
        return self.__camasG * 2 + self.__camasC >= other
    
    def __str__(self):
        return f"Cabaña {self.__numero}: {self.getCapacidad()} personas, {self.__importeXdia:.2f} por día"