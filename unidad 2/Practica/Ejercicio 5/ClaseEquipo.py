class Equipo:
    __EquipoId: str
    __NombreEquipo: str
    __GolesAfavor: int
    __GolesEnContra: int
    __DiferenciaDeGoles: int
    __Puntos: int

    def __init__(self, EquipoId, NombreEquipo, GolesAfavor, GolesEnContra, DiferenciaDeGoles, Puntos):
        self.__EquipoId = EquipoId
        self.__NombreEquipo = NombreEquipo
        self.__GolesAfavor = GolesAfavor
        self.__GolesEnContra = GolesEnContra
        self.__DiferenciaDeGoles = DiferenciaDeGoles
        self.__Puntos = Puntos

    def ID(self):
        # Retorna el id del equipo
        return self.__EquipoId

    def MNombre(self):
        # Retorna el nombre del equipo
        return self.__NombreEquipo

    def GolesF(self):
        # Retorna los goles metidos
        return self.__GolesAfavor

    def GolesC(self):
        # Retorna los goles que le metieron
        return self.__GolesEnContra

    def diferencia(self):
        # Retorna la diferencia entre goles metidos y goles en contra
        return self.__DiferenciaDeGoles

    def Puntos(self):
        # Retorna los puntos que hizo
        return self.__Puntos