class FechaDeFutbol:
    __FechaPartido: str
    __EquipoLocalId: str
    __EquipoVisitanteId: str
    __CantidadGolesLocal: int
    __CantidadGolesVisitante: int

    def __init__(self, FechaPartido, EquipoLocalId, EquipoVisitanteId, CantidadGolesLocal, CantidadGolesVisitante):
        # Constructor de la clase Equipo
        self.__FechaPartido = FechaPartido
        self.__EquipoLocalId = EquipoLocalId
        self.__EquipoVisitanteId = EquipoVisitanteId
        self.__CantidadGolesLocal = CantidadGolesLocal
        self.__CantidadGolesVisitante = CantidadGolesVisitante

    def Fecha(self):
        # Retorna la fecha del partido jugado
        return self.__FechaPartido

    def EquipoLocal(self):
        # Retorna cual es el ID del equipo local
        return self.__EquipoLocalId

    def EquipoVisitante(self):
        # Retorna cual es el ID del equipo visitante
        return self.__EquipoVisitanteId

    def CantidadGolesL(self):
        # Retorna cual es la cantidad de goles que metio el equipo local
        return self.__CantidadGolesLocal

    def CantidadGolesV(self):
        # Retorna cual es la cantidad de goles que metio el equipo visitante
        return self.__CantidadGolesVisitante